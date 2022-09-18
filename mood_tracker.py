import asyncio
# This example uses the sounddevice library to get an audio stream from the
# microphone. It's not a dependency of the project but can be installed with
# `python -m pip install amazon-transcribe aiofile`
# `pip install sounddevice`.
import sounddevice
import text_to_sentiment
import pandas as pd
import skip

from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent

"""
Here's an example of a custom event handler you can extend to
process the returned transcription results as needed. This
handler will simply print the text out to your interpreter.
"""

current_mood = "happy"

moods = ["happy", "sad", "chill", "angry", "stressed"]
mood_tracker = pd.DataFrame(columns=moods)
mood_tracker.loc[len(mood_tracker)] = 0

current_index = 1

def eval_transcript(transcript):
    mood = text_to_sentiment.assess_mood(transcript)
    return mood

def update_mood_tracker(current_index, mood):
    if mood == None:
        exit()        
        
    mood_tracker.iloc[0][mood] += 1

    if mood_tracker.iloc[0]["happy"] > 5:
        past_index = current_index
        current_index = skip.next_song(past_index, "happy")
        mood_tracker.loc[0] = 0 # resets
    if mood_tracker.iloc[0]["sad"] > 5:
        print("change music to sad")
        past_index = current_index
        current_index = skip.next_song(past_index, "sad")
        mood_tracker.loc[0] = 0 # resets
    if mood_tracker.iloc[0]["chill"] > 5:
        print("change music to chill")
        past_index = current_index
        current_index = skip.next_song(past_index, "chill")
        mood_tracker.loc[0] = 0 # resets
    if mood_tracker.iloc[0]["angry"] > 5:
        print("change music to angry")
        past_index = current_index
        current_index = skip.next_song(past_index, "angry")
        mood_tracker.loc[0] = 0 # resets
    if mood_tracker.iloc[0]["stressed"] > 5:
        print("change music to stress")
        past_index = current_index
        current_index = skip.next_song(past_index, "stress")
        mood_tracker.loc[0] = 0 # resets

class MyEventHandler(TranscriptResultStreamHandler):
        
    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        # This handler can be implemented to handle transcriptions as needed.
        # Here's an example to get started.
        results = transcript_event.transcript.results
        for result in results:
            for alt in result.alternatives:
                transcript = alt.transcript
                if transcript != "":
                    #print(transcript)
                    print(eval_transcript(transcript))
                    update_mood_tracker(current_index, eval_transcript(transcript))
                

async def mic_stream():
    # This function wraps the raw input stream from the microphone forwarding
    # the blocks to an asyncio.Queue.
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()

    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(input_queue.put_nowait, (bytes(indata), status))

    # Be sure to use the correct parameters for the audio stream that matches
    # the audio formats described for the source language you'll be using:
    # https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html
    stream = sounddevice.RawInputStream(
        channels=1,
        samplerate=16000,
        callback=callback,
        blocksize=1024 * 2,
        dtype="int16",
    )
    # Initiate the audio stream and asynchronously yield the audio chunks
    # as they become available
    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status


async def write_chunks(stream):
    # This connects the raw audio chunks generator coming from the microphone
    # and passes them along to the transcription stream.
    async for chunk, status in mic_stream():
        await stream.input_stream.send_audio_event(audio_chunk=chunk)
    await stream.input_stream.end_stream()


async def basic_transcribe():
    # Setup up our client with our chosen AWS region
    client = TranscribeStreamingClient(region="us-east-1")

    # Start transcription to generate our async stream
    stream = await client.start_stream_transcription(
        language_code="en-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm"
    )

    # Instantiate our handler and start processing events
    handler = MyEventHandler(stream.output_stream)
    await asyncio.gather(write_chunks(stream), handler.handle_events())


loop = asyncio.get_event_loop()
loop.run_until_complete(basic_transcribe())
loop.close()


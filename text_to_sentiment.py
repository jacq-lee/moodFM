import cohere
from cohere.classify import Example
co = cohere.Client('8HCz6M6p0cecPg6o2qPAfsr7cTu3jZR5No2z7qDp')


def assess_mood(input_str):
    response = co.classify(
        model='large',
        inputs=[input_str],
        examples=[Example("I\'ve had an amazing day.", "happy"), Example("Let\'s go!", "happy"), Example("I\'m so hyped!", "happy"), Example("It\'s so nice to see you.", "happy"), Example("I\'m on top of the world!", "happy"), Example("I missed my bus this morning", "sad"), Example("I\'m not feeling too great today.", "sad"), Example("I\'ve had a slow start to my day.", "sad"), Example("I think I\'m sick.", "sad"), Example("I\'m not feeling myself.", "sad"), Example("Today\'s been pretty normal.", "chill"), Example("I don\'t have much to do today.", "chill"), Example("I\'ve had a good day.", "chill"), Example("I want to dance!", "happy"), Example("Feeling so thankful today.", "happy"), Example("I can\'t wait to see you again!", "happy"), Example("I miss her so much.", "sad"), Example("I\'m vibing today.", "chill"), Example("I feel calm.", "chill"), Example("I can\'t wait to relax and unwind.", "chill"), Example("Are you down to chill this weekend?", "chill"), Example("I\'m cool with anything you decide.", "chill"), Example("Are you free to hangout sometime?", "chill"), Example("I can\'t believe he said that to me!", "angry"), Example("The audacity?", "angry"), Example("I need to relax.", "angry"), Example("I need a nap.", "chill"), Example("I\'m tired.", "chill"), Example("I haven\'t had anything to eat all day!", "angry"), Example("I\'m so mad at them.", "angry"), Example("It\'s been a stressful day.", "stressed"), Example("I have so much to do, where do I start?", "stressed"), Example("I feel so drained.", "stressed"), Example("I\'m burnt out", "stressed"), Example("I\'m cramming for my final in 2 days", "stressed"), Example("I think I\'m going to fail!", "stressed"), Example("I dont know what to do!", "stressed"), Example("This is confusing.", "stressed"), Example("I love Hack The North!", "happy"), Example("I\'m so lonely and scared.", "sad"), Example("Coding is hard.", "stressed"), Example("How am I going to pay rent next month?", "stressed"), Example("This is going terribly.", "stressed"), Example("I\'ll see you later, bye!", "chill"), Example("My dog died.", "sad"), Example("I want to end it all.", "sad"), Example("I am over the moon!", "happy"), Example("They seem nice.", "chill"), Example("Can you listen for once?", "angry"), Example("I\'m going to be late!", "stressed")])
    return(response.classifications[0].prediction)



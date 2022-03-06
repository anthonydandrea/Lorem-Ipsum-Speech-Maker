import lorem
import pyttsx3
import argparse
import random as rd


def get_argparse():
    parser = argparse.ArgumentParser(description='You already know.')
    parser.add_argument('--seconds', '-s', type=float, default=5,
                        help="Number of seconds of audio desired")
    return parser


def get_speech_of_length(seconds):
    p = ' '.join([lorem.sentence() for _ in range(int(seconds+1))])
    p = p.replace('.', ' ')
    words = p.split()
    speech = words[:int(seconds+1)]

    for i in range(len(speech)):
        if rd.random() < 0.3 or i == len(speech) - 1:
            speech[i] = speech[i] + '.'

    return ' '.join(speech)


def main(args):
    engine = pyttsx3.init()
    speech = get_speech_of_length(args.seconds)
    print(f'Speech: {speech}')

    engine.setProperty('rate', 250)

    engine.say(speech)
    engine.runAndWait()


if __name__ == '__main__':
    parser = get_argparse()
    args = parser.parse_args()
    main(args)

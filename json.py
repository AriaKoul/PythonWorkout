import json
import glob

def print_scores(directory):
    scores = {}

    for filename in glob.glob(f'{directory}/*.json'):
        scores[filename] = {}
        f = open(filename)
        with f as input_file:
            for result in json.load(input_file):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)
    
    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores)/len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')
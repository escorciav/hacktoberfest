from pathlib import Path


def parse_tips(folder='tips'):
    "mid-challenge"
    folder = Path(folder)

    tips = []
    for file in folder.glob('*.md'):
        content = open(file, 'r', encoding='utf-8').read()

        hashtags = []
        for word in content.split(' '):
            if len(word) > 1 and word[0] == '#':
                hashtags.append(word.strip())

        tips.append(
            {
               "hastags": ' '.join(hashtags),
               "tip": content
            }
        )
    return tips


if __name__ == '__main__':
    parse_tips('.')
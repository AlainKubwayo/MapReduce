from mrjob.job import MRJob

class wordCount(MRJob):
    def mapper(self, _, line):
        sampleStopWords = ["for", "as", "the", "is", "at", "which", "in", "in", "a", "if", "and", "on", "or", "an"]
        for item in line.split():
            if item.lower() not in sampleStopWords:
                yield(item.lower(), 1)

    def reducer(self, word, counts):
        yield(word, sum(counts))

if __name__ == '__main__':
    wordCount.run()

from mrjob.job import MRJob
from mrjob.step import MRStep


class topTenQuery(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer = self.reducer2)
            ]
   
    def mapper(self, _, line):
        stopWords = ["for", "as", "the", "is", "at", "which", "in", "in", "a", "if", "and", "on", "or", "an"]
        for item in line.split():
            if item.lower() not in stopWords:
                yield(item.lower(), 1)

    def reducer(self, word, counts):
        yield(None, (int(sum(counts)), word))

    def reducer2(self, word, counts):
        a = []
        for count in counts:
          a.append(count)
        temp = []
        for i in range(10):
         temp.append(max(a))
         a.remove(max(a))
        for i in range(10):
          yield temp[i]

if __name__ == '__main__':
    topTenQuery.run()
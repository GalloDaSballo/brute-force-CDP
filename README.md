# CL Data Fetcher

Quickly fetches the data for you to use

Get the timestamp to start

```python
feed = Feed.at("0xaaB2f6b45B28E962B3aCd1ee4fC88aEdDf557756")
latest_round = 36893488147419119266
last_time = 1669064807
while (last_time > 1668804876):
...  (round, answer, start, update, answeredInRound) = feed.getRoundData(latest_round)
...  latest_round -= 1
...  last_time = update
...  print("last_time", last_time)
...  print("answer", answer)
```

## Regex to get CSV Data

Use VS Code Find and Replace

last_time (.*)\n
$1,

answer (.*)
$1,
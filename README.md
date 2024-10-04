# dreye_dictionary
### A dictionary app that support English to Chinese vocabulary lookup

The app search the vocabulary on [Dr.eye](https://yun.dreye.com/ews/index_dict.php).

Currently the search only supports **exact match**.

As the search result is embedded in a HTML (PHP) file. The data is extracted using Python's `beautifulSoup4` package.

The app includes a SQLite database which stores the looked-up result from the source.

When a lookup is requested, the app will check the local database first.
If there is no result found, then it tries to search from the website.

Vocabulary records will be saved into database for later use to speed up the query.

An vocabulary record consists the follwing data:
- `name`: The vocabulary
- `pronunciation`: The representation of the pronunciation
- `content_zh`: Explanation in Chinese
- `content_en`: Explanation in English
- `variant`: Variants of verbs (verbs only)



### Build the app
```bash
docker build -t dreye_dict .
```


### How to use
```bash
docker run --rm dreye_dict <some English word>
```

For example, we lookup a word "vanilla":
```bash
docker run --rm dreye_dict vanilla
```

The output data will be like:
```
vanilla
KK:[vǝˈnɪlǝ]  DJ:[vǝˈnilǝ]
名複: vanillas 

n.
【植】香子蘭；香草[C]
香子蘭浸液；香草精[U]
a.
vanilla
他喜歡香草冰淇淋。
平凡的；普通的；乏味的
```
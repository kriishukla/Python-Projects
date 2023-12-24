{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "gpuClass": "standard"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# NLTK"
      ],
      "metadata": {
        "id": "wCJUE2xdyRjl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "nltk.download('punkt')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nDmG7QsEyb2w",
        "outputId": "720640bb-4880-44d6-81c6-b226dbeb2c42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.tokenize import WordPunctTokenizer\n",
        "tokenizer = WordPunctTokenizer()\n",
        "text = \"Hello, this is NLP Tutorial. I hope you enjoy learning NLP!\"\n",
        "filterdText = tokenizer.tokenize(text)\n",
        "print(filterdText)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QXg4b5BbHPhC",
        "outputId": "eee4fae3-f458-4197-89d1-d3dde59000d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello', ',', 'this', 'is', 'NLP', 'Tutorial', '.', 'I', 'hope', 'you', 'enjoy', 'learning', 'NLP', '!']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.tokenize import word_tokenize\n",
        "\n",
        "text = \"Hello, this is NLP Tutorial. I hope you enjoy learning NLP!\"\n",
        "filterdText = word_tokenize(text)\n",
        "print(filterdText)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kDJe4dGP6JRD",
        "outputId": "0c5daa4a-f53a-4e39-a040-a2c3f4975bd3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello', ',', 'this', 'is', 'NLP', 'Tutorial', '.', 'I', 'hope', 'you', 'enjoy', 'learning', 'NLP', '!']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Sentence Tokenization"
      ],
      "metadata": {
        "id": "FKYFnfLY6lXq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.tokenize import sent_tokenize\n",
        "\n",
        "text = \"Hello everyone, You have done a good job. All the best for future!\"\n",
        "filterdText = sent_tokenize(text)\n",
        "print(filterdText)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QQAdX1sq6pXe",
        "outputId": "47c38b86-0119-425a-979e-200803794379"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello everyone, You have done a good job.', 'All the best for future!']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Removing StopWords"
      ],
      "metadata": {
        "id": "oRoetCYc8PUF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nltk.download('stopwords')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fzUmUTDP6x4E",
        "outputId": "dd5d53c8-5977-4a11-b19f-a72c76ef6a11"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Package stopwords is already up-to-date!\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.corpus import stopwords\n",
        "\n",
        "stop_words = set(stopwords.words('english'))\n",
        "print(stop_words)\n",
        "print(len(stop_words))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wqdPSkgN8Vh8",
        "outputId": "dd7b8e7b-7667-41d4-9e4a-547752dd7c69"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'whom', 'all', 'and', 'most', 'hers', \"wasn't\", 'again', \"shouldn't\", 'do', 'with', 'doesn', 'before', 'further', 'd', 'me', 'how', 'once', 'having', 'it', \"don't\", 'because', 'while', 'itself', 'you', 'has', 'aren', 'that', 'why', 'won', 'a', 'our', \"weren't\", \"you're\", 'here', 'm', \"didn't\", 'haven', 'their', 'during', \"should've\", 'own', 'y', 'couldn', \"mightn't\", \"you've\", 'weren', 'until', 've', 'shan', 'by', 'him', 'on', 'needn', 'to', 'some', 'll', 'other', \"aren't\", 'then', 'than', 'which', 'be', 'doing', 'same', 'very', 'there', 'too', 'between', 'at', \"hadn't\", 'those', 'below', 'just', 'no', 'so', 'ain', 'an', 'i', 'wouldn', 'don', 'now', \"needn't\", 'for', 'o', 'was', 'theirs', 'this', 'these', 'its', 'such', 'up', 'as', 'myself', 're', \"mustn't\", 'of', 'ma', 'down', 'they', \"that'll\", 'when', 'few', \"doesn't\", 'out', 'under', 'her', \"hasn't\", 'but', 'over', 'nor', 'will', 'the', \"won't\", 'have', \"you'd\", 'does', 'only', 'above', 'ourselves', 'mightn', \"wouldn't\", 'yours', \"shan't\", 'against', \"she's\", \"it's\", 'she', 'himself', 'each', 'his', 'my', 't', 'in', 'after', 'themselves', 'wasn', \"haven't\", 'can', 'mustn', \"couldn't\", 'who', 'hasn', 'hadn', 'both', 'ours', 'he', 'had', 'didn', 'yourself', \"you'll\", 'about', 'yourselves', 'your', 'am', 'isn', 'being', 'did', 'into', 'any', 'what', 'herself', 'or', 'not', 'shouldn', \"isn't\", 'are', 'through', 'been', 'if', 's', 'should', 'off', 'where', 'were', 'more', 'from', 'we', 'them', 'is'}\n",
            "179\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.tokenize import word_tokenize\n",
        "\n",
        "input_str = \"NLTK is a leading platform for building Python programs to work with human language data.\"\n",
        "tokens = word_tokenize(input_str)\n",
        "result = [i for i in tokens if i not in stop_words]\n",
        "print (result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "idXeDx0W8bAG",
        "outputId": "47c67b5f-50e3-45d4-efb9-bc955f623937"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['NLTK', 'leading', 'platform', 'building', 'Python', 'programs', 'work', 'human', 'language', 'data', '.']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Stemming\n",
        "Stemming is a process of linguistic normalization, which reduces words to their word root word or chops off the derivational affixes. For example, connection, connected, connecting word reduce to a common word \"connect\"."
      ],
      "metadata": {
        "id": "3ZY2L6dP8ep_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.stem import PorterStemmer\n",
        "\n",
        "stemmer = PorterStemmer()\n",
        "input_str =\"been had done languages cities mice fairly\"\n",
        "input_str = word_tokenize(input_str)\n",
        "for word in input_str:\n",
        "    print(stemmer.stem(word))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kAiW6Qzh8gxG",
        "outputId": "e5f60524-8a05-4d7c-b849-53d0ef258d00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "been\n",
            "had\n",
            "done\n",
            "languag\n",
            "citi\n",
            "mice\n",
            "fairli\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Lemmatization\n",
        "Lemmatization reduces words to their base word, which is linguistically correct lemmas. It transforms root word with the use of vocabulary and morphological analysis. "
      ],
      "metadata": {
        "id": "PXFo05KI8p-c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nltk.download('wordnet')\n",
        "nltk.download('omw-1.4')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J7tmMVvC8oV6",
        "outputId": "30d36930-3afa-4180-c4b6-ed8074fa1204"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package wordnet to /root/nltk_data...\n",
            "[nltk_data]   Package wordnet is already up-to-date!\n",
            "[nltk_data] Downloading package omw-1.4 to /root/nltk_data...\n",
            "[nltk_data]   Package omw-1.4 is already up-to-date!\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.stem import WordNetLemmatizer\n",
        "\n",
        "lemmatizer = WordNetLemmatizer()\n",
        "input_str = \"been had done languages cities mice fairly\"\n",
        "input_str = word_tokenize(input_str)\n",
        "for word in input_str:\n",
        "    print(lemmatizer.lemmatize(word))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2gJ7wcGq8wJg",
        "outputId": "4b560faf-58a5-45b3-f44a-ef9727fef0ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "been\n",
            "had\n",
            "done\n",
            "language\n",
            "city\n",
            "mouse\n",
            "fairly\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Stemming VS Lemmatization\n",
        "Lemmatization is usually more sophisticated than stemming. Stemmer works on an individual word without knowledge of the context. For example, The word \"better\" has \"good\" as its lemma. This thing will miss by stemming because it requires a dictionary look-up."
      ],
      "metadata": {
        "id": "OUMVO3y8KiD9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.corpus import wordnet\n",
        "from nltk.stem.wordnet import WordNetLemmatizer\n",
        "lem = WordNetLemmatizer()\n",
        "\n",
        "from nltk.stem.porter import PorterStemmer\n",
        "stem = PorterStemmer()\n",
        "\n",
        "word = \"better\"\n",
        "\n",
        "print(\"Lemmatized Word:\", lem.lemmatize(word, wordnet.ADJ)) \n",
        "print(\"Stemmed Word:\", stem.stem(word))\n",
        "\n",
        "print()\n",
        "\n",
        "word = \"flying\"\n",
        "print(\"Lemmatized Word:\", lem.lemmatize(word, wordnet.VERB)) \n",
        "print(\"Stemmed Word:\", stem.stem(word))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "45fvoEWZKhYT",
        "outputId": "b2c49829-ae9b-4672-ade3-01670008fc8f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lemmatized Word: good\n",
            "Stemmed Word: better\n",
            "\n",
            "Lemmatized Word: fly\n",
            "Stemmed Word: fli\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Additional Resources. \n",
        "\n",
        "1. [Hands-On nltk tutorial](https://github.com/hb20007/hands-on-nltk-tutorial)\n",
        "2. [Natural Language Toolkit - Tokenizing Text](https://www.tutorialspoint.com/natural_language_toolkit/natural_language_toolkit_tokenizing_text.htm)\n",
        "3. [Text Analytics - nltk](https://www.datacamp.com/tutorial/text-analytics-beginners-nltk)\n",
        "4. [Stemming VS Lemmatization](https://towardsdatascience.com/stemming-vs-lemmatization-in-nlp-dea008600a0)\n"
      ],
      "metadata": {
        "id": "dSuUNYS69m88"
      }
    }
  ]
}
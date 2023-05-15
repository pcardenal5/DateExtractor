# DateExtractor

## Goals

The aim of this projet is to create a program able to extract and parse the dates in a given document. We will focus on legal documents regarding the appraisal of assets. They are written manually and, as such, the date can come in a wide variety of ways. For example, the date 17/05/2023 could be written like "diecisiete de mayo de dos mil veintitrés", "17 de Mayo de 2023", "Diecisiete de Mayo de 2023", etc. Even though all represent the same date finding and parsing the date is a good challenge. 

In this project we will study the different ways this dates could be found and determine which ones are the best, regarding accuracy, ease of use and interpretability.

## Data Set

As previously mentioned, the data set will be comprised of legal documents related to the appraisal of assets called Simple Notes. They contain information about the asset's owner and the legal situation of it. A very important piece of information is the expiration date as it indicates when this situation may change. As has been previously mentioned, there are many ways the date may appear so we will need to consider flexible models that can understand context and exctract meaningful information of it. 

To add to the carrying list of problems, there is no general structure to these documents and they vary widely with the location of the asset. On top of that, some of them don't even have embedded text and we will have to discard them. An alternative could be using an OCR but that is well beyond the scope of this project. Thus, we will need to filter these documents so that we can treat only those whose text can easily be extracted and worked with. 

## Models used

The simplest method of extracting dates we will be using are Regular Expresions, RegEx. They are the cornerstone of many text processing algorithms and we will make the most of them. However, due to the high amount of ways the date can appear the RegEx may become too complex to even be useful. 

Once the RegEx have been taken to their limit we will explore the available resources on Hugging Face. They provide a plethora of transformers that could help us parse the text. On top of that, given the power of those models we may be able to get even more information out of the documents. However, we may be at a disadvantage. These transformers have been made in English so we will have to use a convoluted set of transformers to even start using them. 



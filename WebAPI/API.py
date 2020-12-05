from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import pandas as pd
import numpy as np
from collections import Counter
from itertools import chain
import sister
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle
from xgboost import XGBClassifier
from nltk import word_tokenize, pos_tag
app = Flask(__name__)
CORS(app)


api = Api(app)

class Users(Resource):
    # methods go here
    
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('Key', required=True)  # add args
        parser.add_argument('Template_ques_id', required=True)
        args = parser.parse_args()
        strr = args['Key']
        strrr = args['Template_ques_id']
        print(strr)
        print(strrr)
        print(type(strr))
        def posTagger(df_new):
            tok_and_tag = lambda x: pos_tag(word_tokenize(x))

            df_new['lower_sent'] = df_new['paraphrased_question'].apply(str.lower)
            df_new['tagged_sent'] = df_new['lower_sent'].apply(tok_and_tag)

            possible_tags = sorted(set(list(zip(*chain(*df_new['tagged_sent'])))[1]))

            def add_pos_with_zero_counts(counter, keys_to_add):
                for k in keys_to_add:
                    counter[k] = counter.get(k, 0)
                return counter


            # Detailed steps.
            df_new['pos_counts'] = df_new['tagged_sent'].apply(lambda x: Counter(list(zip(*x))[1]))
            df_new['pos_counts_with_zero'] = df_new['pos_counts'].apply(lambda x: add_pos_with_zero_counts(x, possible_tags))
            df_new['sent_vector'] = df_new['pos_counts_with_zero'].apply(lambda x: [count for tag, count in sorted(x.most_common())])

            # All in one.
            df_new['sent_vector'] = df_new['tagged_sent'].apply(lambda x:
                [count for tag, count in sorted(
                    add_pos_with_zero_counts(
                        Counter(list(zip(*x))[1]), 
                                possible_tags).most_common()
                    )
                ]
            )
            df2 = pd.DataFrame(data = [1],columns = ["id"])
            cols = ['#', '$', "''", '(', ')', ',', '.', ':', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB','``']
            for index,value in df2.iterrows():
                for c in cols:
                    if c in possible_tags:
                        ind = possible_tags.index(c)
                        val = df_new["sent_vector"]
                        print(val)
                        df2.at[index,c] = int(val[0][ind])
                    else:
                        df2.at[index,c] = int(0)
            
            return df2
        def fasttexttagger(df_new):
            embedder = sister.MeanEmbedding(lang="en")
            for index,value in df_new.iterrows():
                sentence = df_new.at[index,"paraphrased_question"]
                vector = embedder(sentence)
                for ind,i in enumerate(vector):
                    df_new.at[index,str(ind)] = i
            
            numerical_cols = ['#', '$', "''", '(', ')', ',', '.', ':', 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', '``']
            for i in range (0,300):
                numerical_cols.append(str(i))
            # scaler = StandardScaler()
            # scaler2 = StandardScaler()
            # scaler.fit(df_AllMain[numerical_cols])
            # df_new[numerical_cols] = scaler.fit_transform(df_new[numerical_cols])
            return df_new

        df_new = pd.DataFrame(data=[strr], columns = ["paraphrased_question"] )
        for index, val in df_new.iterrows():
            df_new.at[index,"template_ques_id"] = int(strrr)
        df2 = posTagger(df_new)
        df_new = df_new.join(df2, how='outer')
        # print(df2)
        df_new = df_new.drop(['lower_sent','tagged_sent','pos_counts',"pos_counts_with_zero","sent_vector","id"], axis=1)
        df_new = fasttexttagger(df_new)
        print(df_new)
        df_new = df_new.drop(["paraphrased_question"], axis = 1)
        loaded_model = pickle.load(open("XGBModel2.sav", "rb"))
        pred = loaded_model.predict(df_new)
        print(pred)
        val = int(pred[0])
        return {'data': val}, 200

api.add_resource(Users, '/users')  # '/users' is our entry point


if __name__ == '__main__':
    app.run()  # run our Flask app
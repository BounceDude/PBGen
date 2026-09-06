
from prompt.abstract.prompt import prompt as abstract_prompt
from prompt.acknowledgment.prompt import prompt as acknowledgment_prompt
from prompt.conclusion.prompt import prompt as conclusion_prompt
from prompt.experiments.prompt import prompt as experiments_prompt
from prompt.introduction.prompt import prompt as introduction_prompt
from prompt.model.prompt import prompt as model_prompt
from prompt.relatework.prompt import prompt as relate_work_prompt


detailed_prompt = "Generate an article according to the following requirements with more than 200 words in each section.\n"\
                  + "\nThe title of this article is 'LawyerGen: Towards Case Summary Generation and Generative Proficiency Assessment for Trial Lawyers'."\
                  + "\nPlease use LaTeX format throughout the entire paper."\
                  + "\nGenerate the abstract according to the following requirements."\
                  + abstract_prompt\
                  + "\nGenerate the introduction according to the following requirements."\
                  + introduction_prompt\
                  + "\nGenerate the relate work section according to the following requirements."\
                  + relate_work_prompt\
                  + "\nGenerate the model section according to the following requirements."\
                  + model_prompt\
                  + "\nGenerate the experiment section according to the following requirements."\
                  + experiments_prompt\
                  + "\nGenerate the summary according to the following requirements."\
                  + conclusion_prompt\
                  + "\nGenerate the acknowledgment according to the following requirements."\
                  + acknowledgment_prompt\
                  + "\nGenerate the reference list."\
                  + "\nGenerate 8 pages of main text. Please refer to https://kdd2027.kdd.org/research-track-call-for-papers/ for details."

# print(detailed_prompt)

from prompt.abstract import prompt as abstract_prompt
from prompt.acknowledgment import prompt as acknowledgment_prompt
from prompt.conclusion import prompt as conclusion_prompt
from prompt.experiments import prompt as experiments_prompt
from prompt.introduction import prompt as introduction_prompt
from prompt.model import prompt as model_prompt
print(__import__("relate work"))
# from prompt.  import prompt as abstract_prompt


detailed_prompt = "Generate an article according to the following requirements.\n"\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the summary according to the following requirements.\n"\
                  + abstract_prompt\
                  + "Generate the reference list."

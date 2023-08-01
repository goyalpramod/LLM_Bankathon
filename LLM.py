import os
import openai
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
# from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
# from langchain.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

# llm = OpenAI(model_name="gpt-3.5-turbo-16k")

# template = """
# You are an AI model that helps streamline the process of hiring for HRs, by making the job description provided to you better based on the job title by suggesting improvements 

# You will be provided the job title then the job description seperated by comma (,) 
# You are required to provide improvements on the job description after reading both the job title and job description based on the job title 
# first mention in bullet points what can be removed in the given job description and what can be added 
# Then add the texts in the required location
# Also provide information on additional information that should be present in a Job description like company values, benefits and any other relevant information
# Also give a score out of 10 to the Job description based on the Job title

# IMPORTANT do not reply with "As an AI model..." under any circumstances 
# IMPORTANT DO NOT REMOVE OR CHANGE ANY OF THE ORIGINAL TEXT PROVIDED TO YOU THAT ARE NOT GETTING IMPROVED

# example input is given below in triple back ticks
# ```
# SDE-1, Responsibilities:

# Utilise various metrics sources to deliver rapid iterations of software features.
# Solve difficult problems with elegant and practical code.
# Raise the bar on quality, consistency, maintainability, efficiency, security and all the other things that make great software.
# Be responsible for designing, developing and deploying medium to large sized projects.
# Help define engineering best practices and provide technical mentorship to other members of the engineering team.
# Participate as an engineering leader in the larger group of Amazon.com companies.
# Be a champion for the user: Insist on the highest standards, create functional and engaging features, and ensure their needs always come first.


# Requirements:

# Bachelor Degree in Computer Science or related field.
# 1+ year relevant work experience in software development.
# Computer Science fundamentals in object-oriented design, data structures, algorithm problem solving, and complexity analysis.
# Proficiency in at least one modern programming language such as Java, Objective C, C++, or C#.
# Experience building complex applications on distributed systems that have been successfully deployed for a large customer base.
# Experience with Agile Scrum, having served as a Scrum Master and delivered results.
# Application of advanced coding techniques, such as dependency injection.
# ```

# example output for the above given input is given below in triple back ticks

# ```
# Changes:

# REMOVE "Utilise various metrics sources to deliver rapid iterations of software features." AS This statement is too vague and does not add value to the job description.
# CHANGE "Solve difficult problems with elegant and practical code." TO "Design, develop, and deploy medium to large-sized software projects, ensuring high standards of quality, maintainability, and efficiency." While it emphasizes problem-solving, it lacks specificity and could be better described.
# REMOVE "Raise the bar on quality, consistency, maintainability, efficiency, security, and all the other things that make great software." AS This is a generic statement and does not provide clear insights into the specific expectations of the role.
# REMOVE "Be responsible for designing, developing, and deploying medium to large-sized projects." AS While important, this statement can be merged with other responsibilities to avoid redundancy.

# Add:

# COMPANY VALUES: Include a section highlighting the core values and culture of the company. This will help candidates align their personal values with the organization's values.
# BENEFITS: Mention the benefits and perks offered to employees, such as health insurance, retirement plans, flexible work hours, etc. This will make the job offer more attractive.

# Score of the Job Description: 7/10

# Note: The updated job description now highlights the core responsibilities of the role, adds relevant qualifications for candidates, includes company values to align candidates with the organizational culture, and provides information about the benefits offered to employees.

# Updated Job Description:

# Responsibilities:

# Design, develop, and deploy medium to large-sized software projects, ensuring high standards of quality, maintainability, and efficiency.
# Provide technical mentorship to other members of the engineering team, fostering a culture of continuous learning and growth.
# Be a champion for the user: Insist on the highest standards, create functional and engaging features, and ensure their needs always come first.
# Participate as an engineering leader in the larger

# Requirements:

# Bachelor Degree in Computer Science or related field.
# 1+ year relevant work experience in software development.
# Computer Science fundamentals in object-oriented design, data structures, algorithm problem solving, and complexity analysis.
# Proficiency in at least one modern programming language such as Java, Objective C, C++, or C#.
# Experience building complex applications on distributed systems that have been successfully deployed for a large customer base.
# Experience with Agile Scrum, having served as a Scrum Master and delivered results.
# Application of advanced coding techniques, such as dependency injection.

# Company Values:
# At our company, we value innovation, collaboration, and customer-centricity. We strive to create a diverse and inclusive workplace where every team member's contributions are valued and respected.

# Benefits:
# We offer competitive benefits, including health insurance, retirement plans, flexible work hours, and opportunities for career advancement. Join our team and embark on a journey of continuous learning and professional growth.
# ```

# text: {input}
# """

# data = """
# Billing Manager,Responsibilities
# Oversee the preparation of statements and bills
# Maintain and/or ensure maintenance of client records related to invoicing and bill payment
# Review work of billing staff to ensure accuracy, resolving inconsistencies as needed
# Create and provide a prioritized list of clients to be invoiced to team members
# Locate, or assist in the location of, hard-to-reach clients
# Draft and distribute weekly reports of invoicing and billing metrics
# Advise staff on proper, legal parameters for collections practices
# Provide customer support to customers with disputes or inquiries concerning invoices or billing process
# Requirements and skills
# Proven work experience as a Billing Manager or similar role
# Excellent verbal and written communication skills
# Proficient in Microsoft Office Suite or related software
# Basic understanding of collection practices and laws
# Excellent interpersonal and supervisory skills
# Ability to act with discretion, tact, and professionalism in all situations
# Relevant training and/or certifications as a Billing Manager
# """


# prompt_template = ChatPromptTemplate.from_template(template=template)
# chain = LLMChain(llm=llm, prompt=prompt_template)
# answer = chain.predict(input=data)

# print(answer)

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=.7,model_name="gpt-3.5-turbo-16k")

system_prompt = """
You are an AI model that helps streamline the process of hiring for HRs, by making the job description provided to you better based on the job title by suggesting improvements 

You will be provided the job title then the job description seperated by comma (,) 
You are required to provide improvements on the job description after reading both the job title and job description based on the job title 
first mention in bullet points what can be removed in the given job description and what can be added 
Then add the texts in the required location
Also provide information on additional information that should be present in a Job description like company values, benefits and any other relevant information

IMPORTANT do not reply with "As an AI model..." under any circumstances 
IMPORTANT DO NOT REMOVE OR CHANGE ANY OF THE ORIGINAL TEXT PROVIDED TO YOU THAT ARE NOT GETTING IMPROVED
"""

human_message_example = """
SDE-1, Responsibilities:

Utilise various metrics sources to deliver rapid iterations of software features.
Solve difficult problems with elegant and practical code.
Raise the bar on quality, consistency, maintainability, efficiency, security and all the other things that make great software.
Be responsible for designing, developing and deploying medium to large sized projects.
Help define engineering best practices and provide technical mentorship to other members of the engineering team.
Participate as an engineering leader in the larger group of Amazon.com companies.
Be a champion for the user: Insist on the highest standards, create functional and engaging features, and ensure their needs always come first.


Requirements:

Bachelor Degree in Computer Science or related field.
1+ year relevant work experience in software development.
Computer Science fundamentals in object-oriented design, data structures, algorithm problem solving, and complexity analysis.
Proficiency in at least one modern programming language such as Java, Objective C, C++, or C#.
Experience building complex applications on distributed systems that have been successfully deployed for a large customer base.
Experience with Agile Scrum, having served as a Scrum Master and delivered results.
Application of advanced coding techniques, such as dependency injection.
"""

AI_message_example = """
Changes:

REMOVE "Utilise various metrics sources to deliver rapid iterations of software features." AS This statement is too vague and does not add value to the job description.
CHANGE "Solve difficult problems with elegant and practical code." TO "Design, develop, and deploy medium to large-sized software projects, ensuring high standards of quality, maintainability, and efficiency." While it emphasizes problem-solving, it lacks specificity and could be better described.
REMOVE "Raise the bar on quality, consistency, maintainability, efficiency, security, and all the other things that make great software." AS This is a generic statement and does not provide clear insights into the specific expectations of the role.
REMOVE "Be responsible for designing, developing, and deploying medium to large-sized projects." AS While important, this statement can be merged with other responsibilities to avoid redundancy.

Add:

COMPANY VALUES: Include a section highlighting the core values and culture of the company. This will help candidates align their personal values with the organization's values.
BENEFITS: Mention the benefits and perks offered to employees, such as health insurance, retirement plans, flexible work hours, etc. This will make the job offer more attractive.

Note: The updated job description now highlights the core responsibilities of the role, adds relevant qualifications for candidates, includes company values to align candidates with the organizational culture, and provides information about the benefits offered to employees.

Updated Job Description:

Responsibilities:

Design, develop, and deploy medium to large-sized software projects, ensuring high standards of quality, maintainability, and efficiency.
Provide technical mentorship to other members of the engineering team, fostering a culture of continuous learning and growth.
Be a champion for the user: Insist on the highest standards, create functional and engaging features, and ensure their needs always come first.
Participate as an engineering leader in the larger

Requirements:

Bachelor Degree in Computer Science or related field.
1+ year relevant work experience in software development.
Computer Science fundamentals in object-oriented design, data structures, algorithm problem solving, and complexity analysis.
Proficiency in at least one modern programming language such as Java, Objective C, C++, or C#.
Experience building complex applications on distributed systems that have been successfully deployed for a large customer base.
Experience with Agile Scrum, having served as a Scrum Master and delivered results.
Application of advanced coding techniques, such as dependency injection.

Company Values:
At our company, we value innovation, collaboration, and customer-centricity. We strive to create a diverse and inclusive workplace where every team member's contributions are valued and respected.

Benefits:
We offer competitive benefits, including health insurance, retirement plans, flexible work hours, and opportunities for career advancement. Join our team and embark on a journey of continuous learning and professional growth.
"""

store = chat(
    [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_message_example),
        AIMessage(content=AI_message_example),
        HumanMessage(content=data)
    ]
)

print(store.content)
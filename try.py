# from Trainer.Train import TrainAI

# TrainAI()

# import markdown

# html = markdown.markdown("hello world")
# print(html)

# from torch import cuda

# print(cuda.is_available())

# from NeuralNetwork.Palm import chatBot
# import markdown
# from markdown.extensions.fenced_code import FencedCodeExtension

# while True:
#     inp = input(">> ")
#     if inp == "exit()":
#         break
#     else:
#         print(markdown.markdown(chatBot(inp), extensions=[FencedCodeExtension()]))

from Trainer.Train import TrainAI

TrainAI()
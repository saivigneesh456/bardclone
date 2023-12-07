from bardapi import Bard
import os
import time

os.environ['_BARD_API_KEY'] = "dwgK4FeK3ArqMEnVzsVehzCpKcZbqfP8FkStLwx5X5d99xCEbye9nlsxKGj5patkbtm35A."

message = input("Ask SP Engine: ")

print(Bard().get_answer(str(message)))
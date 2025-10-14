from functions import *
import time
import datetime



print("Starting data pipeline at:", datetime.datetime.now().strftime)
print("Loading data...")

t0 = time.time()
getVideoIDs()
t1 = time.time()
print("Video IDs loaded in:", str(t1 - t0), "seconds", "\n")

# step 2: extract transcripts for video
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("Step 2: done")
print("Transcripts extracted in:", str(t1 - t0), "seconds", "\n")

# step 3: transform data
t0 = time.time()
transformData()
t1 = time.time()
print("Step 3: done")
print("Data transformed in:", str(t1 - t0), "seconds", "\n")

# step 4: generate text embedings
t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print("Step 4: done")
print("Embeddings generated in:", str(t1 - t0), "seconds", "\n")


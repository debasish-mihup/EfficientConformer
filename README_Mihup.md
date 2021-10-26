How to run the training:

Step 1: Create a sub-directory inside datasets directory with Mihup and then put two further sub-directory with name Training and Evaluation
End of this step you will have two directories with following path available to you
datasets/Mihup/Training
datasets/Mihup/Evaluation

Step 2: Copy all corresponding .txt (with transcription data in librispeech format) and .wav files in the Training directory
datasets/Mihup/Training

Sample .txt file rows (stored according to librispeech format):

i_101_20200319-173446_20200319-173556_20200319-174215_7008373876_Answered-Completed_2802750_5513747_mono_44 əV∇B &L θJ εKS Wəγə μCζ!ə VJOə OəλFSQB &L θJ Ωə!B ΩFB ΩC πCPJQB ∞B
Batch3_093_9928600363_00001072621584629536_mono_2 FζəεJS C&ə∞B C∞ζ!λəOψə∞ə πCWCJ OC ⊂LσC γəΩF&ə φL QλJφC ΩK ∞B φL JOζ!λB Oəλə πJ λəΩJS OC γəζə ζəλə WKζJ OC εKS ζəεəϕə αB λəΩB ΩFS BαəOB WL Mλ@əλə ΩK θJ FζəεJS Bαə ⊂LσC JOζ!λB QλJφC VBΩCJ BαəζJ WC &L γəζə C&ə∞B ΩC ΩBS ζəλə YCOə ΩK &L εKS αFλC OLψCψə OəλFSQB Cζə φBμJ OC Bαə
125.94_128.94_1_i_2020-10-12_10-12-45_8022174628_1602477765.3393_1603436586897_897228_30 LOJ əαBλ!ə βλMεə αəSWBγə ∞Jψə∞əμə γKSOə Mμə πə γKSOζə φC ΩKφə

Step 3: Copy all corresponding .txt (with transcription data in librispeech format) and .wav files in the Evaluation directory
datasets/Mihup/Evaluation

Step 4: Run below command to run the training:

python main.py --config_file configs/EfficientConformerCTCSmall.json

optional arguments: 
--prepare_dataset  (This would create the dataset. Using this command will only create the dataset for files in the .txt files and which haven't been already created)
--re_encode_dataset=True (When enabled with prepare_dataset argument, this would recreate dataset for all files)
--create_tokenizer (Creates the sentencepiece tokenizer)

Note: If now new audio files are added then you only need run main.py with optional arguments once

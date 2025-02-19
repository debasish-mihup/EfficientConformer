# Copyright 2021, Maxime Burchi.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# PyTorch
import torch
import torchaudio

# Sentencepiece
import sentencepiece as spm

# Other
import glob
from tqdm import tqdm
import os

# Mihup 292.367 samples
class MihupDataset(torch.utils.data.Dataset): 
    def __init__(self, dataset_path, training_params, tokenizer_params, split, args):
        self.names = glob.glob(dataset_path + split + "/*.wav")
        self.vocab_type = tokenizer_params["vocab_type"]
        self.vocab_size = str(tokenizer_params["vocab_size"])
        self.lm_mode = training_params.get("lm_mode", False)

        if split.split("-")[0] == "Training":
            self.names = self.filter_lengths(training_params["train_audio_max_length"], training_params["train_label_max_length"], args.rank)
        else:
            self.names = self.filter_lengths(training_params["eval_audio_max_length"], training_params["eval_audio_max_length"], args.rank)

    def __getitem__(self, i):
        if self.lm_mode:
            return [torch.load(self.names[i][:-4] + "." + self.vocab_type + "_" + self.vocab_size)]
        else:
            return [torchaudio.load(self.names[i])[0], torch.load(self.names[i][:-4] + "." + self.vocab_type + "_" + self.vocab_size)]

    def __len__(self):

        return len(self.names)

    def filter_lengths(self, audio_max_length, label_max_length, rank=0):

        if audio_max_length is None or label_max_length is None:
            return self.names

        if rank == 0:
            print("Audio maximum length : {} / Label sequence maximum length : {}".format(audio_max_length, label_max_length))
            self.names = tqdm(self.names)
        # for name in self.names:
        #     print("DEBUG5: ", name, " - ", torch.load(name + "_len"), " < ", audio_max_length, " - ", torch.load(name.replace("wav", self.vocab_type + "_" + self.vocab_size + "_len")), " <= ", label_max_length)
        # print("################### ---------------------- #########################")
        return [name for name in self.names if os.path.isfile(name + "_len") and os.path.getsize(name + "_len") > 0 and torch.load(name + "_len") <= audio_max_length and os.path.isfile(name.replace("wav", self.vocab_type + "_" + self.vocab_size + "_len")) and os.path.getsize(name.replace("wav", self.vocab_type + "_" + self.vocab_size + "_len")) > 0 and torch.load(name.replace("wav", self.vocab_type + "_" + self.vocab_size + "_len")) <= label_max_length]
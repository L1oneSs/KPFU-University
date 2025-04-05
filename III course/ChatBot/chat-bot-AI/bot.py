# # import os
# # import pickle
# # import re
# #
# # import numpy as np
# # import tensorflow as tf
# # import tensorflow_datasets as tfds
# #
# # # Maximum number of samples to preprocess
# # MAX_SAMPLES = 50000
# # # Maximum sentence length
# # MAX_LENGTH = 40
# #
# #
# # def create_datasets():
# #     # Путь к папке с данными
# #     path_to_dataset = "dataset"
# #     path_to_movie_lines = os.path.join(path_to_dataset, 'movie_lines.txt')
# #     path_to_movie_conversations = os.path.join(path_to_dataset, 'movie_conversations.txt')
# #
# #     # Загрузка вопросов и ответов из файлов
# #     questions, answers = load_conversations(path_to_movie_lines, path_to_movie_conversations)
# #
# #     # Создание токенизатора
# #     tokenizer = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(questions + answers, target_vocab_size=2 ** 13)
# #     start_token, end_token = [tokenizer.vocab_size], [tokenizer.vocab_size + 1]
# #     VOCAB_SIZE = tokenizer.vocab_size + 2
# #     questions, answers = tokenize_and_filter(questions, answers, start_token, end_token, tokenizer)
# #
# #     print('Vocab size: {}'.format(VOCAB_SIZE))
# #     print('Number of samples: {}'.format(len(questions)))
# #
# #     # Создание tf.data.Dataset
# #     dataset = tf.data.Dataset.from_tensor_slices((
# #         {
# #             'inputs': questions,
# #             'dec_inputs': answers[:, :-1]
# #         },
# #         {
# #             'outputs': answers[:, 1:]
# #         },
# #     ))
# #     return dataset, tokenizer
# #
# #
# # def preprocess_sentence(sentence):
# #     sentence = sentence.lower().strip()
# #     sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
# #     sentence = re.sub(r'[" "]+', " ", sentence)
# #     sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
# #     sentence = sentence.strip()
# #     return sentence
# #
# #
# # def load_conversations(path_to_movie_lines, path_to_movie_conversations):
# #     id2line = {}
# #     with open(path_to_movie_lines, errors='ignore') as file:
# #         lines = file.readlines()
# #     for line in lines:
# #         parts = line.replace('\n', '').split(' +++$+++ ')
# #         id2line[parts[0]] = parts[4]
# #
# #     inputs, outputs = [], []
# #     with open(path_to_movie_conversations, 'r') as file:
# #         lines = file.readlines()
# #     for line in lines:
# #         parts = line.replace('\n', '').split(' +++$+++ ')
# #         conversation = [line[1:-1] for line in parts[3][1:-1].split(', ')]
# #         for i in range(len(conversation) - 1):
# #             inputs.append(preprocess_sentence(id2line[conversation[i]]))
# #             outputs.append(preprocess_sentence(id2line[conversation[i + 1]]))
# #             if len(inputs) >= MAX_SAMPLES:
# #                 return inputs, outputs
# #     return inputs, outputs
# #
# #
# # def tokenize_and_filter(inputs, outputs, start_token, end_token, tokenizer):
# #     tokenized_inputs, tokenized_outputs = [], []
# #
# #     for (sentence1, sentence2) in zip(inputs, outputs):
# #         sentence1 = start_token + tokenizer.encode(sentence1) + end_token
# #         sentence2 = start_token + tokenizer.encode(sentence2) + end_token
# #         if len(sentence1) <= MAX_LENGTH and len(sentence2) <= MAX_LENGTH:
# #             tokenized_inputs.append(sentence1)
# #             tokenized_outputs.append(sentence2)
# #
# #     tokenized_inputs = tf.keras.preprocessing.sequence.pad_sequences(
# #         tokenized_inputs, maxlen=MAX_LENGTH, padding='post')
# #     tokenized_outputs = tf.keras.preprocessing.sequence.pad_sequences(
# #         tokenized_outputs, maxlen=MAX_LENGTH, padding='post')
# #
# #     return tokenized_inputs, tokenized_outputs
# #
# #
# # def build_model(vocab_size, embedding_dim, enc_units, batch_size):
# #     # Define the encoder
# #     encoder_inputs = tf.keras.layers.Input(shape=(None,))
# #     encoder_embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)(encoder_inputs)
# #     encoder = tf.keras.layers.LSTM(enc_units, return_state=True)
# #     encoder_outputs, state_h, state_c = encoder(encoder_embedding)
# #     encoder_states = [state_h, state_c]
# #
# #     # Define the decoder
# #     decoder_inputs = tf.keras.layers.Input(shape=(None,))
# #     decoder_embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)(decoder_inputs)
# #     decoder_lstm = tf.keras.layers.LSTM(enc_units, return_sequences=True, return_state=True)
# #     decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
# #     decoder_dense = tf.keras.layers.Dense(vocab_size, activation='softmax')
# #     decoder_outputs = decoder_dense(decoder_outputs)
# #
# #     # Define the model
# #     model = tf.keras.models.Model([encoder_inputs, decoder_inputs], decoder_outputs)
# #     return model
# #
# # def main():
# #     # Create dataset and tokenizer
# #     dataset, tokenizer = create_datasets()
# #
# #     # Define model parameters
# #     vocab_size = tokenizer.vocab_size
# #     embedding_dim = 128
# #     enc_units = 256
# #     batch_size = 64
# #
# #     # Build the model
# #     model = build_model(vocab_size, embedding_dim, enc_units, batch_size)
# #
# #     # Compile the model
# #     model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
# #
# #     # Prepare dataset for training
# #     train_dataset = dataset.map(lambda x, y: ({'input_1': tf.expand_dims(x['inputs'], axis=0),
# #                                                'input_2': tf.expand_dims(x['dec_inputs'], axis=0)},
# #                                               {'dense': tf.expand_dims(y['outputs'], axis=0)}))
# #
# #     # Train the model
# #     model.fit(train_dataset, epochs=1)
# #
# #     # Save the model
# #     model.save("chatbot_model")
# #
# #     # Save tokenizer
# #     with open('tokenizer.pickle', 'wb') as handle:
# #         pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
# #
# #         # Загрузка модели и токенизатора
# #         model = tf.keras.models.load_model("chatbot_model")
# #         with open('tokenizer.pickle', 'rb') as handle:
# #             tokenizer = pickle.load(handle)
# #
# #         # Примеры диалогов для тестирования
# #         dialogues = [
# #             ("Привет!", "Привет, как дела?"),
# #             ("Как твое настроение?", "Отлично, спасибо! А у тебя?"),
# #             ("Что делаешь?", "Просто отдыхаю. Ты чем занят?"),
# #             ("Я хочу поесть", "Может быть сходишь в ресторан?"),
# #         ]
# #
# #         # Тестирование
# #         for question, expected_response in dialogues:
# #             response = generate_response(question, model, tokenizer)
# #             print(f"Вопрос: {question}")
# #             print(f"Ожидаемый ответ: {expected_response}")
# #             print(f"Ответ модели: {response}")
# #             print()
# #
# #
# #
# # def preprocess_sentence(sentence):
# #     sentence = sentence.lower().strip()
# #     sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
# #     sentence = re.sub(r'[" "]+', " ", sentence)
# #     sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
# #     sentence = sentence.strip()
# #     return sentence
# #
# #
# # def generate_response(input_text, model, tokenizer):
# #     # Преобразование текста в числовой формат с помощью токенизатора
# #     input_sequence = tokenizer.encode(preprocess_sentence(input_text))
# #     input_sequence = tf.keras.preprocessing.sequence.pad_sequences([input_sequence], maxlen=MAX_LENGTH, padding='post')
# #
# #     # Создание заглушки для предыдущего ответа (можно использовать пустой массив)
# #     dummy_prev_response = np.zeros((1, MAX_LENGTH))
# #
# #     # Предсказать ответ от модели чатбота
# #     predicted_response = model.predict([input_sequence, dummy_prev_response], verbose=0)[0]
# #
# #     # Преобразование индексов слов в строки с помощью токенизатора
# #     response_text = tokenizer.decode([i for i in np.argmax(predicted_response, axis=1) if i < tokenizer.vocab_size])
# #
# #     return response_text
# #
# # if __name__ == "__main__":
# #     tf.executing_eagerly()
# #     main()
# #
# #
# #
#
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import csv
import random
import re
import os
import unicodedata
import codecs
import itertools

CUDA = torch.cuda.is_available()
print(CUDA)
device = torch.device("cuda" if CUDA else "cpu")

corpus_name = "cornell movie-dialogs corpus"
corpus = os.path.join("data", corpus_name)
lines_filepath = os.path.join(corpus, "movie_lines.txt")
conv_filepath = os.path.join(corpus, "movie_conversations.txt")
# visualizing some lines
with open(lines_filepath, 'r') as file:
    lines = file.readlines()
for line in lines[:10]:
    print(line.strip())

# splits each line of the file into a dictionary of fields(lineID,characterID,movieID,character,text)
line_fields = ["lineID", "characterID", "movieID", "character", "text"]
lines = {}

with open(lines_filepath, 'r', encoding='iso-8859-1') as f:
    for line in f:
        values = line.split(" +++$+++ ")
        # Extract fields
        lineObj = {}
        for i, field in enumerate(line_fields):
            lineObj[field] = values[i]
        lines[lineObj['lineID']] = lineObj
# Grouping fields of lines from the above loaded lines into conversation based on "movie_conversations.txt"

conv_fields = ["character1ID", "character2ID", "movieID", "utteranceIDs"]
conversations = []

with open(conv_filepath, 'r', encoding='iso-8859-1') as f:
    for line in f:
        values = line.split(" +++$+++ ")
        # Extract fields
        convObj = {}
        for i, field in enumerate(conv_fields):
            convObj[field] = values[i]
        lineIds = eval(convObj["utteranceIDs"])
        # Reassemble lines
        convObj["lines"] = []
        for lineId in lineIds:
            convObj["lines"].append(lines[lineId])
        conversations.append(convObj)
# Extracts pairs of sentences from conversations
qa_pairs = []
for conversation in conversations:
    # Iterate over all the lines of the conversation
    for i in range(len(conversation["lines"]) - 1):  # We ignore the last line (no answer for it)
        inputLine = conversation["lines"][i]["text"].strip()
        targetLine = conversation["lines"][i + 1]["text"].strip()
        # Filter wrong samples (if one of the lists is empty)
        if inputLine and targetLine:
            qa_pairs.append([inputLine, targetLine])
# Define path to new file
datafile = os.path.join(corpus, "formatted_movie_lines.txt")

delimiter = '\t'
# Unescape the delimiter
delimiter = str(codecs.decode(delimiter, "unicode_escape"))

# Writing the conversational pairs into new csv file
print("\nWriting newly formatted file...")
with open(datafile, 'w', encoding='utf-8') as outputfile:
    writer = csv.writer(outputfile, delimiter=delimiter)
    for pair in qa_pairs:
        writer.writerow(pair)

# visualizing some lines
with open(datafile, 'rb') as file:
    lines = file.readlines()
for line in lines[:10]:
    print(line.strip())

# Default word tokens
PAD_token = 0  # Used for padding short sentences
SOS_token = 1  # Start-of-sentence token
EOS_token = 2  # End-of-sentence token


class Vocabulary:
    def __init__(self, name):
        self.name = name
        self.trimmed = False
        self.word2index = {}
        self.word2count = {}
        self.index2word = {PAD_token: "PAD", SOS_token: "SOS", EOS_token: "EOS"}
        self.num_words = 3  # Counting SOS, EOS, PAD

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.num_words
            self.word2count[word] = 1
            self.index2word[self.num_words] = word
            self.num_words += 1
        else:
            self.word2count[word] += 1

    # Removing words below a certain count threshold
    def trim(self, min_count):
        if self.trimmed:
            return
        self.trimmed = True

        keep_words = []

        for k, v in self.word2count.items():
            if v >= min_count:
                keep_words.append(k)

        print('keep_words {} / {} = {:.4f}'.format(
            len(keep_words), len(self.word2index), len(keep_words) / len(self.word2index)
        ))

        # Reinitializing dictionaries
        self.word2index = {}
        self.word2count = {}
        self.index2word = {PAD_token: "PAD", SOS_token: "SOS", EOS_token: "EOS"}
        self.num_words = 3  # Counting default tokens

        for word in keep_words:
            self.addWord(word)


# Turn a Unicode string to plain ASCII
def unicodeToAscii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


# Testing the function - eliminates special characters
unicodeToAscii("cédillea")
'cedillea'


# Lowercase, trim, and remove non-letter characters
def normalizeString(s):
    # Unicode string to plain ASCII
    s = unicodeToAscii(s.lower().strip())

    # Replacing any .!? by a whitespace plus the character
    # ' \1' means the first bracketed group
    # r is not to consider ' \1' as an individual character
    # r in r" \1" is to esccape the backslash
    s = re.sub(r"([.!?])", r" \1", s)

    # Removing any character that is not a sequence of lower or upper case letters
    # + means one or more
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)

    # Removing a sequence of whitespace characters
    s = re.sub(r"\s+", r" ", s).strip()

    return s


# Testing the function
normalizeString("aaa1103!?.     aaa'a aaa?")
'aaa ! ? . aaa a aaa ?'
datafile = os.path.join(corpus, "formatted_movie_lines.txt")

# Reading the file and splitting into lines
print("Reading and processing file....Please Wait")
lines = open(datafile, encoding='utf-8').read().strip().split('\n')

# Splitting every line into pairs and normalizing them
pairs = [[normalizeString(s) for s in pair.split('\t')] for pair in lines]

print("Done Reading!!!")
voc = Vocabulary(corpus)

MAX_LENGTH = 10  # Maximum sentence length to consider


# Returns True iff both sentences in a pair 'p' are under the MAX_LENGTH threshold
def filterPair(p):
    # Input sequences need to preserve the last word for EOS token
    if p:
        return len(p[0].split(' ')) < MAX_LENGTH and len(p[1].split(' ')) < MAX_LENGTH
    else:
        return False


# Filter pairs using filterPair condition
def filterPairs(pairs):
    pairs = [pair for pair in pairs if pair != ['']]
    return [pair for pair in pairs if filterPair(pair)]


print("There are {} pairs/conversations in the dataset".format(len(pairs)))
pairs = filterPairs(pairs)
print("After filtering there are {} pairs/conversations".format(len(pairs)))

for pair in pairs:
    voc.addSentence(pair[0])
    voc.addSentence(pair[1])

print("Counted words:", voc.num_words)
for pair in pairs[:10]:
    print(pair)

MIN_COUNT = 3  # Minimum word count threshold for trimming


def trimRareWords(voc, pairs, MIN_COUNT):
    # Trim words used under the MIN_COUNT from the voc
    voc.trim(MIN_COUNT)
    # Filter out pairs with trimmed words
    keep_pairs = []
    for pair in pairs:
        input_sentence = pair[0]
        output_sentence = pair[1]
        keep_input = True
        keep_output = True
        # Check input sentence
        for word in input_sentence.split(' '):
            if word not in voc.word2index:
                keep_input = False
                break
        # Check output sentence
        for word in output_sentence.split(' '):
            if word not in voc.word2index:
                keep_output = False
                break

        # Only keep pairs that do not contain trimmed word(s) in their input or output sentence
        if keep_input and keep_output:
            keep_pairs.append(pair)

    print("Trimmed from {} pairs to {}, {:.4f} of total".format(len(pairs), len(keep_pairs),
                                                                len(keep_pairs) / len(pairs)))
    return keep_pairs


# Trim voc and pairs
pairs = trimRareWords(voc, pairs, MIN_COUNT)



def indexesFromSentence(voc, sentence):
    return [voc.word2index[word] for word in sentence.split(' ')] + [EOS_token]


indexesFromSentence(voc, pairs[1][0])
[7, 8, 9, 10, 4, 11, 12, 13, 2]


def zeroPadding(l, fillvalue=PAD_token):
    return list(itertools.zip_longest(*l, fillvalue=fillvalue))


def binaryMatrix(l, value=PAD_token):
    m = []
    for i, seq in enumerate(l):
        m.append([])
        for token in seq:
            if token == PAD_token:
                m[i].append(0)
            else:
                m[i].append(1)
    return m


# Returns padded input sequence tensor and lengths
def inputVar(l, voc):
    indexes_batch = [indexesFromSentence(voc, sentence) for sentence in l]
    lengths = torch.tensor([len(indexes) for indexes in indexes_batch])
    padList = zeroPadding(indexes_batch)
    padVar = torch.LongTensor(padList)
    return padVar, lengths


# Returns padded target sequence tensor, padding mask, and max target length
def outputVar(l, voc):
    indexes_batch = [indexesFromSentence(voc, sentence) for sentence in l]
    max_target_len = max([len(indexes) for indexes in indexes_batch])
    padList = zeroPadding(indexes_batch)
    mask = binaryMatrix(padList)
    mask = torch.ByteTensor(mask)
    padVar = torch.LongTensor(padList)
    return padVar, mask, max_target_len


# Returns all items for a given batch of pairs
def batch2TrainData(voc, pair_batch):
    pair_batch.sort(key=lambda x: len(x[0].split(" ")), reverse=True)
    input_batch, output_batch = [], []
    for pair in pair_batch:
        input_batch.append(pair[0])
        output_batch.append(pair[1])
    inp, lengths = inputVar(input_batch, voc)
    output, mask, max_target_len = outputVar(output_batch, voc)
    return inp, lengths, output, mask, max_target_len


# Example for validation
small_batch_size = 5
batches = batch2TrainData(voc, [random.choice(pairs) for _ in range(small_batch_size)])
input_variable, lengths, target_variable, mask, max_target_len = batches

print("input_variable:", input_variable)
print("lengths:", lengths)
print("target_variable:", target_variable)
print("mask:", mask)
print("max_target_len:", max_target_len)



class EncoderRNN(nn.Module):
    def __init__(self, hidden_size, embedding, n_layers=1, dropout=0):
        super(EncoderRNN, self).__init__()
        self.n_layers = n_layers
        self.hidden_size = hidden_size
        self.embedding = embedding

        # Initialize GRU; the input_size and hidden_size params are both set to 'hidden_size'
        #   because our input size is a word embedding with number of features == hidden_size
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers, dropout=(0 if n_layers == 1 else dropout),
                          bidirectional=True)

    def forward(self, input_seq, input_lengths, hidden=None):
        # Convert word indexes to embeddings
        embedded = self.embedding(input_seq)
        # Pack padded batch of sequences for RNN module
        packed = torch.nn.utils.rnn.pack_padded_sequence(embedded, input_lengths)
        # Forward pass through GRU
        outputs, hidden = self.gru(packed, hidden)
        # Unpack padding
        outputs, _ = torch.nn.utils.rnn.pad_packed_sequence(outputs)
        # Sum bidirectional GRU outputs
        outputs = outputs[:, :, :self.hidden_size] + outputs[:, :, self.hidden_size:]
        # Return output and final hidden state
        return outputs, hidden


# Luong attention layer
class Attn(torch.nn.Module):
    def __init__(self, method, hidden_size):
        super(Attn, self).__init__()
        self.method = method
        if self.method not in ['dot', 'general', 'concat']:
            raise ValueError(self.method, "is not an appropriate attention method.")
        self.hidden_size = hidden_size
        if self.method == 'general':
            self.attn = torch.nn.Linear(self.hidden_size, hidden_size)
        elif self.method == 'concat':
            self.attn = torch.nn.Linear(self.hidden_size * 2, hidden_size)
            self.v = torch.nn.Parameter(torch.FloatTensor(hidden_size))

    def dot_score(self, hidden, encoder_output):
        return torch.sum(hidden * encoder_output, dim=2)

    def general_score(self, hidden, encoder_output):
        energy = self.attn(encoder_output)
        return torch.sum(hidden * energy, dim=2)

    def concat_score(self, hidden, encoder_output):
        energy = self.attn(torch.cat((hidden.expand(encoder_output.size(0), -1, -1), encoder_output), 2)).tanh()
        return torch.sum(self.v * energy, dim=2)

    def forward(self, hidden, encoder_outputs):
        # Calculate the attention weights (energies) based on the given method
        if self.method == 'general':
            attn_energies = self.general_score(hidden, encoder_outputs)
        elif self.method == 'concat':
            attn_energies = self.concat_score(hidden, encoder_outputs)
        elif self.method == 'dot':
            attn_energies = self.dot_score(hidden, encoder_outputs)

        # Transpose max_length and batch_size dimensions
        attn_energies = attn_energies.t()

        # Return the softmax normalized probability scores (with added dimension)
        return F.softmax(attn_energies, dim=1).unsqueeze(1)


class LuongAttnDecoderRNN(nn.Module):
    def __init__(self, attn_model, embedding, hidden_size, output_size, n_layers=1, dropout=0.1):
        super(LuongAttnDecoderRNN, self).__init__()

        # Keep for reference
        self.attn_model = attn_model
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers
        self.dropout = dropout

        # Define layers
        self.embedding = embedding
        self.embedding_dropout = nn.Dropout(dropout)
        self.gru = nn.GRU(hidden_size, hidden_size, n_layers, dropout=(0 if n_layers == 1 else dropout))
        self.concat = nn.Linear(hidden_size * 2, hidden_size)
        self.out = nn.Linear(hidden_size, output_size)

        self.attn = Attn(attn_model, hidden_size)

    def forward(self, input_step, last_hidden, encoder_outputs):
        # Note: we run this one step (word) at a time
        # Get embedding of current input word
        embedded = self.embedding(input_step)
        embedded = self.embedding_dropout(embedded)
        # Forward through unidirectional GRU
        rnn_output, hidden = self.gru(embedded, last_hidden)
        # Calculate attention weights from the current GRU output
        attn_weights = self.attn(rnn_output, encoder_outputs)
        # Multiply attention weights to encoder outputs to get new "weighted sum" context vector
        context = attn_weights.bmm(encoder_outputs.transpose(0, 1))
        # Concatenate weighted context vector and GRU output using Luong eq. 5
        rnn_output = rnn_output.squeeze(0)
        context = context.squeeze(1)
        concat_input = torch.cat((rnn_output, context), 1)
        concat_output = torch.tanh(self.concat(concat_input))
        # Predict next word using Luong eq. 6
        output = self.out(concat_output)
        output = F.softmax(output, dim=1)
        # Return output and final hidden state
        return output, hidden


def maskNLLLoss(inp, target, mask):
    nTotal = mask.sum()
    crossEntropy = -torch.log(torch.gather(inp, 1, target.view(-1, 1)))
    loss = crossEntropy.masked_select(mask).mean()
    loss = loss.to(device)
    return loss, nTotal.item()


def train(input_variable, lengths, target_variable, mask, max_target_len, encoder, decoder, embedding,
          encoder_optimizer, decoder_optimizer, batch_size, clip, max_length=MAX_LENGTH):
    # Zero gradients
    encoder_optimizer.zero_grad()
    decoder_optimizer.zero_grad()

    # Set device options
    input_variable = input_variable.to(device)
    lengths = lengths.to(device)
    target_variable = target_variable.to(device)
    mask = mask.to(device)

    # Initialize variables
    loss = 0
    print_losses = []
    n_totals = 0

    # Forward pass through encoder
    encoder_outputs, encoder_hidden = encoder(input_variable, lengths)

    # Create initial decoder input (start with SOS tokens for each sentence)
    decoder_input = torch.LongTensor([[SOS_token for _ in range(batch_size)]])
    decoder_input = decoder_input.to(device)

    # Set initial decoder hidden state to the encoder's final hidden state
    decoder_hidden = encoder_hidden[:decoder.n_layers]

    teacher_forcing_ratio = 0.5

    # Determine if we are using teacher forcing this iteration
    use_teacher_forcing = True if random.random() < teacher_forcing_ratio else False

    # Forward batch of sequences through decoder one time step at a time
    if use_teacher_forcing:
        for t in range(max_target_len):
            decoder_output, decoder_hidden = decoder(
                decoder_input, decoder_hidden, encoder_outputs
            )
            # Teacher forcing: next input is current target
            decoder_input = target_variable[t].view(1, -1)
            # Calculate and accumulate loss
            mask_loss, nTotal = maskNLLLoss(decoder_output, target_variable[t], mask[t])
            loss += mask_loss
            print_losses.append(mask_loss.item() * nTotal)
            n_totals += nTotal
    else:
        for t in range(max_target_len):
            decoder_output, decoder_hidden = decoder(
                decoder_input, decoder_hidden, encoder_outputs
            )
            # No teacher forcing: next input is decoder's own current output
            _, topi = decoder_output.topk(1)
            decoder_input = torch.LongTensor([[topi[i][0] for i in range(batch_size)]])
            decoder_input = decoder_input.to(device)
            # Calculate and accumulate loss
            mask_loss, nTotal = maskNLLLoss(decoder_output, target_variable[t], mask[t])
            loss += mask_loss
            print_losses.append(mask_loss.item() * nTotal)
            n_totals += nTotal

    # Perform backpropatation
    loss.backward()

    # Clip gradients: gradients are modified in place
    _ = torch.nn.utils.clip_grad_norm_(encoder.parameters(), clip)
    _ = torch.nn.utils.clip_grad_norm_(decoder.parameters(), clip)

    # Adjust model weights
    encoder_optimizer.step()
    decoder_optimizer.step()

    return sum(print_losses) / n_totals


def trainIters(model_name, voc, pairs, encoder, decoder, encoder_optimizer, decoder_optimizer, embedding,
               encoder_n_layers, decoder_n_layers, save_dir, n_iteration, batch_size, print_every, save_every, clip,
               corpus_name, loadFilename):
    # Load batches for each iteration
    training_batches = [batch2TrainData(voc, [random.choice(pairs) for _ in range(batch_size)])
                        for _ in range(n_iteration)]

    # Initializations
    print('Initializing ...')
    start_iteration = 1
    print_loss = 0
    if loadFilename:
        start_iteration = checkpoint['iteration'] + 1

    # Training loop
    print("Training...")
    for iteration in range(start_iteration, n_iteration + 1):
        training_batch = training_batches[iteration - 1]
        # Extract fields from batch
        input_variable, lengths, target_variable, mask, max_target_len = training_batch

        # Run a training iteration with batch
        loss = train(input_variable, lengths, target_variable, mask, max_target_len, encoder,
                     decoder, embedding, encoder_optimizer, decoder_optimizer, batch_size, clip)
        print_loss += loss

        # Print progress
        if iteration % print_every == 0:
            print_loss_avg = print_loss / print_every
            print("Iteration: {}; Percent complete: {:.1f}%; Average loss: {:.4f}".format(iteration,
                                                                                          iteration / n_iteration * 100,
                                                                                           print_loss_avg))
            print_loss = 0

        # Save checkpoint
        if (iteration % save_every == 0):
            directory = os.path.join(save_dir, model_name, corpus_name,
                                     '{}-{}_{}'.format(encoder_n_layers, decoder_n_layers, hidden_size))
            if not os.path.exists(directory):
                os.makedirs(directory)
            torch.save({
                'iteration': iteration,
                'en': encoder.state_dict(),
                'de': decoder.state_dict(),
                'en_opt': encoder_optimizer.state_dict(),
                'de_opt': decoder_optimizer.state_dict(),
                'loss': loss,
                'voc_dict': voc.__dict__,
                'embedding': embedding.state_dict()
            }, os.path.join(directory, '{}_{}.tar'.format(iteration, 'checkpoint')))


class GreedySearchDecoder(nn.Module):
    def __init__(self, encoder, decoder):
        super(GreedySearchDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, input_seq, input_length, max_length):
        # Forward input through encoder model
        encoder_outputs, encoder_hidden = self.encoder(input_seq, input_length)
        # Prepare encoder's final hidden layer to be first hidden input to the decoder
        decoder_hidden = encoder_hidden[:decoder.n_layers]
        # Initialize decoder input with SOS_token
        decoder_input = torch.ones(1, 1, device=device, dtype=torch.long) * SOS_token
        # Initialize tensors to append decoded words
        all_tokens = torch.zeros([0], device=device, dtype=torch.long)
        all_scores = torch.zeros([0], device=device)
        # Iteratively decode one word token at a time
        for _ in range(max_length):
            # Forward pass through decoder
            decoder_output, decoder_hidden = self.decoder(decoder_input, decoder_hidden, encoder_outputs)
            # Obtain most likely word token and its softmax score
            decoder_scores, decoder_input = torch.max(decoder_output, dim=1)
            # Record token and score
            all_tokens = torch.cat((all_tokens, decoder_input), dim=0)
            all_scores = torch.cat((all_scores, decoder_scores), dim=0)
            # Prepare current token to be next decoder input (add a dimension)
            decoder_input = torch.unsqueeze(decoder_input, 0)
        # Return collections of word tokens and scores
        return all_tokens, all_scores


def evaluate(encoder, decoder, searcher, voc, sentence, max_length=MAX_LENGTH):
    ### Format input sentence as a batch
    # words -> indexes
    indexes_batch = [indexesFromSentence(voc, sentence)]
    # Create lengths tensor
    lengths = torch.tensor([len(indexes) for indexes in indexes_batch])
    # Transpose dimensions of batch to match models' expectations
    input_batch = torch.LongTensor(indexes_batch).transpose(0, 1)
    # Use appropriate device
    input_batch = input_batch.to(device)
    lengths = lengths.to(device)
    # Decode sentence with searcher
    tokens, scores = searcher(input_batch, lengths, max_length)
    # indexes -> words
    decoded_words = [voc.index2word[token.item()] for token in tokens]
    return decoded_words


def evaluateInput(encoder, decoder, searcher, voc):
    input_sentence = ''
    while (1):
        try:
            # Get input sentence
            input_sentence = input('> ')
            # Check if it is quit case
            if input_sentence == 'q' or input_sentence == 'quit': break
            # Normalize sentence
            input_sentence = normalizeString(input_sentence)
            # Evaluate sentence
            output_words = evaluate(encoder, decoder, searcher, voc, input_sentence)
            # Format and print response sentence
            output_words[:] = [x for x in output_words if not (x == 'EOS' or x == 'PAD')]
            print('Bot:', ' '.join(output_words))

        except KeyError:
            print("Error: Encountered unknown word.")


# Configure models
model_name = 'cb_model'
attn_model = 'dot'
# attn_model = 'general'
# attn_model = 'concat'
hidden_size = 500
encoder_n_layers = 2
decoder_n_layers = 2
dropout = 0.1
batch_size = 32
save_dir = os.path.join("data", "save")

# NOTE : Set checkpoint to load from; set to None if starting from scratch
# loadFilename = None
checkpoint_iter = 8000
loadFilename = os.path.join(save_dir, model_name, corpus_name,
                            '{}-{}_{}'.format(encoder_n_layers, decoder_n_layers, hidden_size),
                            '{}_checkpoint.tar'.format(checkpoint_iter))

# Load model if a loadFilename is provided
if loadFilename:
    # If loading on same machine the model was trained on
    #checkpoint = torch.load(loadFilename)
    # If loading a model trained on GPU to CPU
    checkpoint = torch.load(loadFilename, map_location=torch.device('cpu'))
    encoder_sd = checkpoint['en']
    decoder_sd = checkpoint['de']
    encoder_optimizer_sd = checkpoint['en_opt']
    decoder_optimizer_sd = checkpoint['de_opt']
    embedding_sd = checkpoint['embedding']
    voc.__dict__ = checkpoint['voc_dict']

print('Building encoder and decoder ...')
# Initialize word embeddings
embedding = nn.Embedding(voc.num_words, hidden_size)
if loadFilename:
    embedding.load_state_dict(embedding_sd)
# Initialize encoder & decoder models
encoder = EncoderRNN(hidden_size, embedding, encoder_n_layers, dropout)
decoder = LuongAttnDecoderRNN(attn_model, embedding, hidden_size, voc.num_words, decoder_n_layers, dropout)
if loadFilename:
    encoder.load_state_dict(encoder_sd)
    decoder.load_state_dict(decoder_sd)
# Use appropriate device
encoder = encoder.to(device)
decoder = decoder.to(device)
print('Models built and ready to go!')

# Set dropout layers to eval mode
encoder.eval()
decoder.eval()

# Initialize search module
searcher = GreedySearchDecoder(encoder, decoder)

# Begin chatting
#evaluateInput(encoder, decoder, searcher, voc)
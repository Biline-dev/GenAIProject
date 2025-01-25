from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

def calculate_bleu(reference, hypothesis):
    return sentence_bleu([reference.split()], hypothesis.split())

def calculate_rouge(reference, hypothesis):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    return scorer.score(reference, hypothesis)

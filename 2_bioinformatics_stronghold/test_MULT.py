def multiple_alignment(word_list):
    '''Returns the multiple alignment of a given list of words.'''
    from itertools import product
    from operator import add, mul
    from scipy.misc import comb
    from functools import reduce
    from rosalind_utils import print_matrix
    
    # There are some issues scoring the first symbols, so force a match here and remove it from the alignment later.
    word_list = ['$'+word for word in word_list]
    
    # Initialize scoring and backtrack dictionaries, along with the indices and base score.
    S, backtrack = {}, {}
    perm_list = list(product([0, -1], repeat=len(word_list)))[1:]
    base_score = -1*comb(len(word_list), 2, exact=True)
    print('base_score =', base_score)
    
    for index in product(*map(range,map(lambda s: len(s) + 1, word_list))):
       
       # We forced a match with the first symbols, so the zero-shell should lead to the zero index.
        if reduce(mul, index) == 0:
            # Since we forced a match with the first symbol, we want to force starting point to be the zero index.
            if sum(index) == 0:
                # All symbols match.
                S[index] = 0
            else:
                # Make it smaller than the lowest possible score.
                S[index] = 2*base_score*reduce(add, map(len, word_list))
        else:
            # Use previous scores to determine the best score for the current index.
            previous_scores = [S[tuple(map(add, index, perm))] for perm in perm_list]
            current_index_scores = []
            for perm in perm_list:
                chars = [word_list[i][index[i]-1] if perm_value == -1 else '-' for i, perm_value in enumerate(perm)]
                current_index_scores.append(base_score + sum([comb(chars.count(ch), 2, exact=True) for ch in set(chars)]))
            
            scores = map(add, previous_scores, current_index_scores)
            backtrack[index], S[index] = max(enumerate(scores), key=lambda p: p[1])
    
    print_matrix(perm_list)    
    
    # Initialize the alignment and indicies.   
    alignment = word_list
    current_index = list(map(len, word_list))
    
    # Get the max score.
    # Note: The forced match at start of each word does not change the max score, as matched symbols have a score of zero.
    max_score = S[tuple(current_index)]
    
    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]
    
    # Insert indels to get the alignment.
    while reduce(mul, current_index) != 0:
        for i, perm_value in enumerate(perm_list[backtrack[tuple(current_index)]]):
            if perm_value == 0:
                alignment[i] = insert_indel(alignment[i], current_index[i])
            else:
                current_index[i] -= 1
    
    # Note: We don't need to prepend any indels because we forced a match at the start of all words.
    # Remove the forced match from all alignments to recover the correct alignment.
    return [str(max_score)] + [aligned[1:] for aligned in alignment]

if __name__ == '__main__':
    #from scripts import ReadFASTA
    from rosalind_utils import parse_fasta
    
    # Parse the input data.
    #words = [fasta[1] for fasta in ReadFASTA('data/rosalind_mult.txt')]
    words = parse_fasta('problem_datasets/rosalind_mult.txt')
    
    # Get the alignment. 
    words_aligned = multiple_alignment(words)
    
    # Print and save the answer.
    print('\n'.join(words_aligned))
    with open('output/085_MULT.txt', 'w') as output_data:
        output_data.write('\n'.join(words_aligned))
#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Global Alignment with Constant Gap Penalty
URL: http://rosalind.info/problems/gcon/

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
Return: The maximum alignment score between s and t. Use:
    The BLOSUM62 scoring matrix.
    Constant gap penalty equal to 5.
'''

'''
EXAMPLE INPUT:
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY

EXAMPLE OUTPUT:
13
'''

from rosalind_utils import parse_fasta, print_matrix

def scoring_matrix(path):
    ''' Format a mutli-line text file containing substitution scores
        into a dictonary.
    '''
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    costs = {}
    for i in lines:
        l = i.split(' ')
        costs[' '.join(l[:2])] = l[2]

    return(costs)


def get_score(matrix, a, b, gap=-5):
    ''' Retrieve the score from the scoring matrix. '''
    if a == '-' or b == '-':
        return(gap)
    else:
        key = ' '.join((a, b))
        cost = matrix[key]

    return(int(cost))


def alignment_score(s, t, matrix, gap, gap_e=0):
    ''' Returns two matrices of the edit distance and edit alignment between
        strings s and t.
    '''

    # Initialize the matrices with zeros.
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    gap_s = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    gap_t = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    # Start with gap penalty as False
    penalty = False
    
    for i in range(1, len(s)+1):
        d[i][0] = gap
    for j in range(1, len(t)+1):
        d[0][j] = gap

    # Fill in the score matrix.
    n = 0
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            cost = [ d[i-1][j-1] + get_score(matrix, s[i-1], t[j-1], gap),
                     d[i-1-n][j] + gap + (n-1)*gap_e,
                     d[i][j-1-n] + gap + (n-1)*gap_e ]
            d[i][j] = max(cost)
            if cost.index(d[i][j]) != 0:
                n += 1
            else:
                n = 0

    print_matrix(d, s, t)

    # The max possible score is found at the bottom-right corner of the matrix
    return(d[-1][-1])


def main():
    #s, t = parse_fasta('problem_datasets/rosalind_gcon.txt', True) #2701.891
    s, t =['PLEASANTLY', 'MEANLY']
    print('\n'.join((s, t)))
    scores = scoring_matrix('data/BLOSUM62.txt')

    max_score = alignment_score(s, t, scores, -5)
    print(max_score)
    

if __name__ == '__main__':
    main()

'''
GFFSQNWELFHENEWAYAKYNAEWFSLCKPEHLTKEIGPFVHQECPRPIWVNMMSSILTPDADSYCMIYAHRVQFIAEAVTLTHSYCHENAPHTAMRTHMWGMIIAYDENWDQQTHRQHYTIWDTFHNWHKETPPDGQDNDRTMSCYYQMDPQWCGKFLIREHVDTFHMCNWFFHMFIPNFAYGCRTFNTNNQDASMRHWSKFWVAIIEVSQPRNIQKIFKGATANHDQHEGWAYVSYLRKNWVDGERFIWAFLHKKMLTDSYAKLVMKFLPAGDQWRAQLHEPTEDEYLTQDLITDGGCNESDDTKLYHRFVTDKMRRLICYVGHHALTKTDYECNWYYDTICCAELWQQCVNFIEDNSGYLNDWFANLFFVASEANHFRMQPRHQKCCHGESVTAKCHVQPFSDGDDPRYPCGDQGYLYQQGNYCKYIYTEHSQNHPSQYTPSKKNEFRKYHGDYNEYARHAFKIEIREGNRCWNVWVHVIMVYELLHQCAVALHAIKMQFCRNQDKHWCFRPITTMMTILVIQLFLRHLFSGSAAFHLVWDSCAHCIGPRMEQAAFWAWGTSIHTGCEGAKQSMAGFTARFFDYPVKNHQRKNSVPCRTIQVFPVFKWLWLDRIVDSIQTEWQETHKHENTFHRNPDWVVRIREDSEYNLACKHALPIPALNFCSYWFPAVIIDEHKYPNMKWCQGPEVQPESCEGDKNTKMNFEKMAGWDTSMFAWPMGRPCWPGQMHITEIVRYHSHMEKR
GFFWQCDSRRLAWENEWAVVMKYNLTQFSLCKPCHYTKEIPFVHQECPMIHNPHVHFDSILTPDADSYCMIYAHRVQVITHSYCHPENAPHKAMRTHMWGMIIAYDEMWDQQTHRQHYTIWDCFINWHKETCYYQMDPQWCGKFLIREHVDTFHMDNWFFFMDTGDYILGIPNFAYGCRFLTNNQDASMRKPPWMDKQCIFSDDRGMMPIIQNHDQWNMMKFLPCEADIKSYLRKNWVDGERFIWALLHQVWNICNCALVMKFNQWQAQLHEPTNCYVRNRAFLITDLQVYVHECYFGQKLRPIHRFVTDNMRRLICYVGHHALTKTDYECNWYRDDLRLPKELDFNMWERFLWWCEMNQQSWESNSGYLNDWFANLFFVASESNHFRMTPRHQYCCHGESVNAKCHVQPFSDGDNPPYWLDGKRKRRYPLYQQYYWMDCKYIYTEHSQNHPLQYTPSSKNEFRKYHGDYNEYARHAFKIQHSACWNYWVRRWSWYKGVILLHQGKYMDHVDCDIFPHRPDKHWVSTYSRCFRPITCMMTILVLFLRGRRILTHETYEWRYAGFSGSEAFVLVWDSCAHCIKPRMEQAAFWAWGTSRCPTHHTHCEGCKQRMAWFHCFTARFFDYISVELGKQKQNSVPCRTIQVIPVFKWLWLDRIVDTHWHQNTFHRNPDWVMKFVMCLACKHALPIVGYDYHHHQALNFCSYWFPAVIIDEEVCPESCEGNKNTKMNFISACEWNKMAGWDTSMLCAWPMGQMHITEIVRYHINHMEKR
= ~2701
'''

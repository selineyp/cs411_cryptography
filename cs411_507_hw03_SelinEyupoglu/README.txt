question_1.py: it outputs the period of the polynomial given in the question, it also outputs the states of the first period.

question_2.py: it uses the BM algorithm and outputs the length of the shortest LFSR and the connection polynomial.

question_3.py : it takes the ciphertext in the question and considers the first 84 bits of the ciphertext since 'Dear Student' is 84 bits long. Then it considers the first 11 bits of the XORed sequence and reverse it, because the output sequence is reversed in the LFSR. Then it finds the key by applying LFSR, then decryption is done by XOR operation with the key.

question_4.py : it performs polynomial multiplication and reduces them in GF(2^8).for part b of the question, it multiplies two polynomials that were claimed to be inverses of each other in GF(2^8), then outputs the resulting polynomial is equivalent to 1.

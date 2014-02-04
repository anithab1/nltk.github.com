# Natural Language Toolkit: code_modal_tabulate

 def tabulate(cfdist, words, categories):
     print('%-16s' % 'Category', end=' ')                    # column headings
     for word in words:
         print('%6s' % word, end=' ')
     print
     for category in categories:
         print('%-16s' % category, end=' ')                  # row heading
         for word in words:                                  # for each word
             print('%6d' % cfdist[category][word], end=' ')  # print table cell
         print                                               # end the row


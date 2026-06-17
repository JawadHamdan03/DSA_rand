## longest unique substr
# dynamic sliding window

def longest_unique_substr(word : str):
    l=0
    st= dict()
    longest=0
    for r in range(len(word)):
        if word[r] not in st:
            st[word[r]]=1
        else :
            st[word[r]]+=1
            while st[word[r]] > 1:
                st[word[l]]-=1
                l+=1
        longest=max(longest,r-l+1)
    return longest



print(longest_unique_substr("abcabcqbb"))
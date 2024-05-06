class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for i in range(len(s)):
            #initialise variables
            freq_groups=collections.defaultdict(int)
            char_freq={}
            max_freq,min_freq=1,1
            char_freq[s[i]]=1
            freq_groups[char_freq[s[i]]]=1

            for j in range(i+1,len(s)):
                if s[j] not in char_freq:
                    char_freq[s[j]]=1
                    min_freq=min(min_freq,1)
                    freq_groups[char_freq[s[j]]]+=1
                    ans+=max_freq-min_freq
                    
                else:
                    freq_groups[char_freq[s[j]]]-=1
                    if freq_groups[char_freq[s[j]]]==0 and min_freq==char_freq[s[j]]:
                        min_freq+=1
                    char_freq[s[j]]+=1
                    freq_groups[char_freq[s[j]]]+=1
                    max_freq=max(char_freq[s[j]],max_freq)
                    ans+=max_freq-min_freq
        return ans 
        
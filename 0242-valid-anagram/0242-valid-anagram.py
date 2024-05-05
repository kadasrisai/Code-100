class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def countt(s):
		f_dict={}
		for i in s:
			if i in f_dict:
				f_dict[i]+=1
			else:
				f_dict[i]=1
		return f_dict
	f_dict1=countt(s)
	f_dict2=countt(t)

	return f_dict1 == f_dict2
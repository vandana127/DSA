class Solution {
public:
    int strStr(string haystack, string needle) {
        long i=0;
        long j=0;
        int count=0;
       while (i<haystack.size() && j<needle.size())
       {
           if (haystack[i]==needle[j])
           {
               count++;
               j++;
           }
           else
           {
               j=0;
               i=i-count;
               count=0;
           }
           i++;
       }
        if(j==count and j==needle.size())
        {
            return i-count;
        }
        
        return -1;
    }
};

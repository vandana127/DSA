/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *newnode=head;
        ListNode *newnode2=head;
       if(head==NULL|| head->next==NULL)return NULL;
       for(int i=0;i<n;i++)
       {
           newnode=newnode->next;
       }
        if(newnode==NULL)return head->next;
        while(newnode->next!=NULL)
        {
            newnode=newnode->next;
            newnode2=newnode2->next;
        }
        newnode2->next=newnode2->next->next;
        return head;
        
    } 
};

/* https://leetcode.com/problems/string-to-integer-atoi/
*
*  Faster than 100.00% of C online submissions.
*
*  Memory Usage less than 65.26% of C online submissions.
*
*/
int myAtoi(char * s)
{
    int integer = 0;
    
    if(*s == NULL) return 0;
    
    for(int i = 0 ; ; i++)
    {
        if(*(s + i) >= '0' && *(s + i) <= '9')
        {
            if(integer > 100000000 || integer < -100000000)
            {
                if((*s == '-' ? -((double)integer * 10 + *(s + i) - '0') : (double)integer * 10 + *(s + i) - '0') <= INT_MIN) return INT_MIN;
                else if((*s == '-' ? -((double)integer * 10 + *(s + i) - '0') : (double)integer * 10 + *(s + i) - '0') >= INT_MAX) return INT_MAX;
            }

            integer = integer * 10 + (*(s + i) - '0');
            
            if(*(s + 1) != '`' && i >= 1){*(s + 1) = '`';}
            else if(*(s + 1) != '`' && *(s) != '`')*(s) = '`';
        }
        else if(integer == 0 && *(s + 1) != '`' && (*s != '`') && *(s + i) == ' '
                ||
                (*(s + i) == '-' && (*(s + 1) != '`') && (*(s) != '`') && (*(s + i + 1) >= '0' && *(s + i + 1) <= '9'))
                ||
                (*(s + i) == '+' && (*(s + 1) != '`') && (*(s) != '`') && (*(s + i + 1) >= '0' && *(s + i + 1) <= '9')))
        {if(*(s + i) == '-')*(s) = '-';continue;}
        else
        {
            return integer == 0 ? integer : *s == '-' ? -integer : integer;
        }
    }
}

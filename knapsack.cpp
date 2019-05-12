#include <iostream>
using namespace std;
int main()
{int sack[10][10],i,j,x,y,n,c,w[10],v[10];
cout<<"enter  the number of items"<<endl;cin>>n;
cout<<"enter  the sack capacity"<<endl;cin>>c;
for(i=1;i<=n;i++)
{ cout<<"enter the "<<i<<"th element value"<<endl;
cin>>v[i];
cout<<"enter the "<<i<<"th element weight"<<endl;
cin>>w[i];
}
for(i=0;i<=n;i++)
 {
for(j=0;j<=c;j++)
    sack[i][j]=0;
 }
for(i=1;i<=n;i++)
{
    for(j=1;j<=c;j++)
    {
        if(j-w[i]>=0)
        {
            x=v[i]+sack[i-1][j-w[i]];
            y=sack[i-1][j];
            if(x>y)
                sack[i][j]=x;
            else
                sack[i][j]=y;
        }
        else
            sack[i][j]=sack[i-1][j];
    }
}
cout<<endl<<"the optimal solution is "<<sack[n][c];
cout<<endl<<endl;
j=c;i=n;
while(j>0 and i>0)
{
    if(sack[i][j]==sack[i-1][j])
    {
        i--;
    }
    else
    {
      cout<<i<<" is selected"<<endl;
      j=j-w[i];
      i--;
    }
}
return 0;
}


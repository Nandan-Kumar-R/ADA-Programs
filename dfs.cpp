#include <iostream>
using namespace std;
int a[10][10],v[10],n;
void dfs(int i)
{int j;
    v[i]=1;
    for(j=0;j<n;j++)
    {
        if(a[i][j]==1 && v[j]==0)
            dfs(j);
    }
    cout<<i<<" ";
}
int main()
{
    int i,j,count=0;
    cout<<"enter the number of nodes"<<endl;
    cin>>n;
    cout<<"enter the adjacency matrix"<<endl;
    for(i=0;i<n;i++)
    { v[i]=0;
        for(j=0;j<n;j++)
            cin>>a[i][j];
    }
    for(i=0;i<n;i++)
    {
        if(v[i]==0)
        { count++;
         dfs(i);
         cout<<endl;

        }
    }
    if(count==1)
        cout<<"connected"<<endl;
    else
        cout<<"disconnected"<<endl;

    return 0;
}

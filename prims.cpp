#include<iostream>
using namespace std;
int a,b,u,v,n,i,j,ne=1;
int visited[10]={0},min1,mincost=0,cost[10][10];
int main()
{
        cout<<"\nEnter the number of nodes:";
        cin>>n;
        cout<<"\nEnter the adjacency matrix:\n";
        for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        {
             cin>>cost[i][j];
                if(cost[i][j]==0)
                 cost[i][j]=999;
        }
        visited[1]=1;
        cout<<"\n";
        while(ne < n)
        {
                for(i=1,min1=999;i<=n;i++)
                for(j=1;j<=n;j++)
                if(cost[i][j]< min1 && visited[i]!=0)
                {
                        min1=cost[i][j];
                        a=u=i;
                        b=v=j;
                }

                if(visited[u]==0 || visited[v]==0)
                {
                        cout<<"\nEdge "<<ne++<<":("<<a<<"-->"<<b<<") "<<"cost:"<<min1<<endl;
                        mincost+=min1;
                        visited[b]=1;
                }
                cost[a][b]=cost[b][a]=999;
        }
        cout<<"\nMinimun cost="<<mincost;
        return 0;
}

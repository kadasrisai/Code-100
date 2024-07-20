class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dfs(sv,visited,path):
            visited[sv]=1
            path[sv]=1
            for u in adj[sv]:
                if visited[u]==0:
                    if dfs(u,visited,path):
                        return True
                elif path[u]==1:
                    return True
            path[sv]=0
            return False
        
        adj=[[] for i in range(numCourses)]
        n=len(prerequisites)
        for i in range(n):
            u,v=prerequisites[i][0],prerequisites[i][1]
            adj[v].append(u)
        visited=[0]*numCourses
        path=[0]*numCourses
        for i in range(numCourses):
            if visited[i]==0:
                if dfs(i,visited,path):
                    return False
        return True
        
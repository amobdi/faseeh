#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("test.xml", "r", stdin);
	string src, dst;
	map<string, set<string> > Map;
	map<string, set<string> >::iterator it;
	set<string>::iterator sit;
	while(cin >> src >> dst) {
		Map[src].insert(dst);
	}
	for(it = Map.begin(); it != Map.end(); it++) {
		printf("	<category>\n"); 
		printf("		<pattern>* %s *</pattern>\n", it->first.c_str());
		printf("		<template>\n");
		for(sit = it->second.begin(); sit != it->second.end() ; sit++) {
			printf("			<srai><star index=\"1\"/> %s <star index=\"2\"/></srai>\n", sit->c_str());
		}
		printf("		</template>\n");
		printf("	</category>\n"); 
	}
	return 0;
}
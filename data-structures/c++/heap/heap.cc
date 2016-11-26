#include<vector>
#include<string>
#include<iostream>
#include<random>

struct Node
{
    int key;
    std::string name;
    Node(int pk, std::string str): key(pk), name(str) {} 
};

std::vector<Node> build_nodes(const std::vector<std::string> names)
{
    std::vector<Node> heap;
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> uni(0, 20);
    for (std::string name: names)
    {
        Node node = Node(uni(rng), name);
        std::cout << '\n' << "built node with pk of " << node.key;
        heap.push_back(node);
    }
    return heap;
}

int main()
{
    std::vector<std::string> names = {"Jordan", "Leah", "Michael"};
    build_nodes(names);
    std::cout << '\n';
    return 0;
}


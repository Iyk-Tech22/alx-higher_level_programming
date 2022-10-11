#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* Struct prototype */
typedef struct node
{
    int num;
    struct node *next;
}node_list;

/* add node prototype */
node_list *add_node(node_list **h, int data);
size_t print_node(node_list *head);
void free_node(node_list *head);
int check_cycle(node_list *head);

#endif

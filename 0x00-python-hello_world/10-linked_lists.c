#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_node - add a new node to the list
 * @head: pointer to head
 * @data: data to add
 * Return: newly add node
 */
node_list *add_node(node_list **head, int data)
{
    node_list *new_node;

    new_node = malloc(sizeof(node_list));
    if (!new_node)
		return (NULL);

    new_node->num = data;
    new_node->next = *head;
    *head = new_node;
    return (new_node);
}

/**
 * print_node - print all node in list
 * @head: pointer to a node
 * Return: numbers of node in list
 */
 size_t print_node(node_list *head)
 {
    int n_node = 0;
    node_list *current_node;

    current_node = head;
    while(current_node)
    {
        printf("%d\n", current_node->num);
        current_node = current_node->next;
        ++n_node;
    }
    return (n_node);
 }

 /**
  * free_node - free node from memory
  * @head: head node of the list
  */
  void free_node(node_list *head)
  {
    node_list *next_node;

    next_node = head;
    while (head)
    {
        next_node = head->next;
        free(head);
        head = next_node;
    }
  }
/**
   * check_cycle - checks if a list is a cycle
   * @head: pointer to the first node
   * Return: 0 if not cycle or 1 if cycle
   */
  int check_cycle(node_list  *head)
  {
    node_list *node;
    int is_circle;
    
    node = head;
    is_circle = 0;
    do
    {
        node = node->next;
    }
    while (node != head && node != NULL);

    if (node == NULL)
        return (is_circle);
    is_circle = 1;
    return (is_circle);
  }

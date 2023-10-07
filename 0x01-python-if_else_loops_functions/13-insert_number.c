#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert node into the list
 * @head: pointer to the head node
 * @number: integer value to be added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	prev->next = new_node;
	new_node->next = current;

	return (new_node);
	return (new_node);
}

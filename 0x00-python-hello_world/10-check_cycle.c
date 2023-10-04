#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if the linked list has a cycle
 * @list: pointer to the head of th list
 * Return: 1 if success 0 if fail
 */
int check_cycle(listint_t *list)
{
	listint_t *new, *temp;

	if (list == NULL)
		return (0);
	temp = list;
	new = list;
	while (new != NULL && new->next != NULL)
	{
		temp = temp->next;
		new = new->next->next;
		if (temp == new)
			return (1);
	}
	return (0);
}

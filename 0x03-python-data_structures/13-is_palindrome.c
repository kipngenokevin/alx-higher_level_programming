#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_list - reverse list
 * @head: pointer to filetype listint
 * Return: previous
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if its palindrom
 * @head: pointer to pointer of head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head, *fast = *head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *second_half = reverse_list(slow);

	while (second_half)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}
	return (1);
}

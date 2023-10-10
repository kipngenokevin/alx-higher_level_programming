#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * reverse_list - reverse the list
 * @head: pointer of the head element
 * Return: pointer to prev
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - check if it is palindrome
 * @head: pointer to pointer of head element
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;
	listint_t *second_half = NULL;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_list(slow);
	while (second_half)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}
	return (1);
}

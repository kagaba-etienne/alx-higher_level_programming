#include "lists.h"

/**
 * is_palindrome - check if singly linked list is palindrome
 * @head: head of the linked list
 * Return: 0 or 1 depending on the list
 */

int is_palindrome(listint_t **head)
{
	int length;
	int i;
	int j;
	int finish;
	listint_t *current;
	listint_t *temp;

	current = *head;
	temp = *head;
	length = (int)print_listint(*head);
	if (1)
	{
		for (i = 0; i <= (length / 2); i++)
		{
			if (length % 2 == 1)
				finish = (2 * (length / 2)) - i;
			else
				finish = (2 * (length / 2)) - i - 1;
			for (j = 0; j < finish; j++)
				temp = temp->next;
			if (temp->n == current->n)
			{
				current = current->next;
				temp = *head;
				continue;
			}
			else
			{
				return (0);
			}
		}
	}
	return (1);
}

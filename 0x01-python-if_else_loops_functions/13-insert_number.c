#include "lists.h"
#include<stdlib.h>
#include<stddef.h>

/**
 * insert_node - inserting node in singly linked list
 * @head: the adress of head
 * @number: number to insert in the list
 * Return: return address to inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	int i;
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	temp = *head;
	i = 0;
	while (current != NULL)
	{
		if (current->n >= new->n)
		{
			if (i == 0)
			{
				*head = new;
				new->next = current
				return (new);
			}
			temp->next = new;
			new->next = current;
			return (new);
		}
		else
		{
			if (i > 0)
				temp = temp->next;
			current = current->next;
			i++;
		}
	}
	current->next = new;
	return (new);
}

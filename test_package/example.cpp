#include <iostream>
#include <libfoo/libfoo.h>

int main() {
	libfoo::run_me();

	if (libfoo::answer_to_question_of_life() != 42)
	{
		std::cout << "ERROR: answer_to_question_of_life() returned "
				  << libfoo::answer_to_question_of_life()
				  << " instead of 42" << std::endl;
		return 1;
	}

	return 0;
}

#include <iostream>

#include "libfoo.h"

namespace libfoo
{
	void run_me()
	{
		std::cout << "Hello from libfoo!" << std::endl;
	}

	int answer_to_question_of_life()
	{
		return 43;
	}
}

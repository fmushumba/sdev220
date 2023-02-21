{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2249830d-4f29-4b17-b1f3-5dbefe13659b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'my_sum'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_31900\\3419481271.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mfractions\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mFraction\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mmy_sum\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msum\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mclass\u001b[0m \u001b[0mTestSum\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0munittest\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mTestCase\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'my_sum'"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "from fractions import Fraction\n",
    "\n",
    "from my_sum import sum\n",
    "\n",
    "class TestSum(unittest.TestCase):\n",
    "    def test_list_int(self):\n",
    "        \"\"\"\n",
    "        Test that it can sum a list of integers\n",
    "        \"\"\"\n",
    "        data = [1, 2, 3]\n",
    "        result = sum(data)\n",
    "        self.assertEqual(result, 6)\n",
    "\n",
    "    def test_list_fraction(self):\n",
    "        \"\"\"\n",
    "        Test that it can sum a list of fractions\n",
    "        \"\"\"\n",
    "        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]\n",
    "        result = sum(data)\n",
    "        self.assertEqual(result, 1)    \n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd30b2a9-8282-4064-b8eb-f6df9f6985c2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

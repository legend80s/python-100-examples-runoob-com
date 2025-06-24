function permute(arr, size = arr.length) {
	if (arr.length === 0 || arr.length === 1) {
		return [arr];
	}

	const result = [];

	for (let index = 0; index < arr.length; index++) {
		const num = arr[index];

		const without = arr.slice(0, index).concat(arr.slice(index + 1));
		const rest = permute(without, size - 1);
		// console.log('rest:', rest);

		for (const numbers of rest) {
			result.push([num, ...numbers.slice(0, size - 1)]);

			// if (Array.isArray(numbers)) {
			//   result.push([num,  ...numbers])
			// } else {
			//   result.push([num,  numbers])
			// }
		}
	}

	return result;
}

// console.log('permute:', permute([1, 2, 3], 2));
// console.log('permute:', permute([1, 2, 3, 4], 3));

it("permute", () => {
	const expected = [
		[1, 2, 3],
		[1, 2, 4],
		[1, 3, 2],
		[1, 3, 4],
		[1, 4, 2],
		[1, 4, 3],
		[2, 1, 3],
		[2, 1, 4],
		[2, 3, 1],
		[2, 3, 4],
		[2, 4, 1],
		[2, 4, 3],
		[3, 1, 2],
		[3, 1, 4],
		[3, 2, 1],
		[3, 2, 4],
		[3, 4, 1],
		[3, 4, 2],
		[4, 1, 2],
		[4, 1, 3],
		[4, 2, 1],
		[4, 2, 3],
		[4, 3, 1],
		[4, 3, 2],
	];

	expect(permute([1, 2, 3, 4], 3)).toEqual(expected);
});

function permuteBacktrace(arr, size = arr.length) {
	const result = [];
	const path = [];
	const used = [];

	function backtrace() {
		if (path.length === size) {
			result.push([...path]);
			return;
		}

		for (let i = 0; i < arr.length; i++) {
			const num = arr[i];
			if (used[num]) continue;

			path.push(num);
			used[num] = true;
			backtrace();
			used[num] = false;
			path.pop();
		}
	}

	backtrace(0);

	return result;
}

it("permuteBacktrace without size", () => {
	const expected = [
		[1, 2, 3],
		[1, 3, 2],
		[2, 1, 3],
		[2, 3, 1],
		[3, 1, 2],
		[3, 2, 1],
	];

	const actual = permuteBacktrace([1, 2, 3]);
	console.log("actual:", actual);

	expect(actual).toEqual(expected);
	expect(permuteBacktrace([1, 2, 3], 1)).toEqual([[1], [2], [3]]);
	expect(permuteBacktrace([1, 2, 3], 2)).toEqual([
		[1, 2],
		[1, 3],
		[2, 1],
		[2, 3],
		[3, 1],
		[3, 2],
	]);
});

it("permuteBacktrace with size", () => {
	const expected = [
		[1, 2, 3],
		[1, 2, 4],
		[1, 3, 2],
		[1, 3, 4],
		[1, 4, 2],
		[1, 4, 3],
		[2, 1, 3],
		[2, 1, 4],
		[2, 3, 1],
		[2, 3, 4],
		[2, 4, 1],
		[2, 4, 3],
		[3, 1, 2],
		[3, 1, 4],
		[3, 2, 1],
		[3, 2, 4],
		[3, 4, 1],
		[3, 4, 2],
		[4, 1, 2],
		[4, 1, 3],
		[4, 2, 1],
		[4, 2, 3],
		[4, 3, 1],
		[4, 3, 2],
	];

	expect(permuteBacktrace([1, 2, 3, 4], 3)).toEqual(expected);
});

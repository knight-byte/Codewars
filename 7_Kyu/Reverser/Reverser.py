def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    return int(''.join([i for i in str(n)])[::-1])

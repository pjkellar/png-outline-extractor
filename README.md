# Black Only

Converts .PNG files with color, keeping ONLY the black content (or almost perfect black with a threshold)

# Usage

### Build the Dockerfile

```bash
docker build -t black-only-png .
```

### Example Run for Pure Black

```bash
docker run --rm \
  -v "$(pwd)/input_pngs:/in" \
  -v "$(pwd)/output_black:/out" \
  black-only-png --in /in --out /out
```

### Example Run for _almost_ Pure Black (Anti-Aliased Edges)


```bash
docker run --rm \
  -v "$(pwd)/input_pngs:/in" \
  -v "$(pwd)/output_black:/out" \
  black-only-png --in /in --out /out --threshold 20
  ```
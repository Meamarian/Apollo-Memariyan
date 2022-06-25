# Task.3

Here, I will explain where we should make changes in order to achieve the goal of task 3.
## Which File? What kind of Scheduler?

One of the schedulers that we can use is the SchedulerLocalRes. We can see it's source code [Here](https://github.com/Apollo-Core/SC-Core/blob/263e10604f4129a2da722789b90ddcc5e4bd9276/src/main/java/at/uibk/dps/sc/core/scheduler/SchedulerLocalRes.java). there is a comment here that guide us. it says: 

```bash
/**
 * This scheduler places the tasks preferably on local resources (or more
 * precisely, the available resources with limited capacity); Remote resources
 * are used only after exceeding the capacity of available local resources.
 * 
 * @author Fedor Smirnov
 */
```
As a result, if we change this condition ( if: we have capacity mappings -> use one of those / else ... ) to the desired condition ( if: we have 10 capacity mappings -> use one of those/ else use remote serverless resource ... ), the problem will be solved.
## Important Part of Code

```java
  @Override
  protected Set<Mapping<Task, Resource>> chooseMappingSubset(final Task task,
      final Set<Mapping<Task, Resource>> mappingOptions) {
    final List<Mapping<Task, Resource>> actualOptions = new ArrayList<>();
    if (mappingOptions.stream().anyMatch(this::isCapacityMapping)) {
      // we have capacity mappings -> use one of those
      actualOptions.addAll(
          mappingOptions.stream().filter(this::isCapacityMapping).collect(Collectors.toSet()));
    } else {
      actualOptions.addAll(mappingOptions);
    }
    final int idx = rand.nextInt(actualOptions.size());
    final Set<Mapping<Task, Resource>> result = new HashSet<>();
    result.add(actualOptions.get(idx));
    return result;
  }
```

import Pkg
Pkg.add("Primes")

using Distributed
addprocs(7)

@everywhere using Primes
@everywhere function solution(s::Int64, e::Int64) Int64
                total = 0
                for i in (s + 1):e
                    if i == 1 || maximum(Primes.factor(Set, i)) < √i
                        total += 1
                    end
                end
                return total
            end

function problem668Parallel()
    local jobs = RemoteChannel(() -> Channel{Int}(32))
    local results = RemoteChannel(() -> Channel{Tuple}(32))

    @everywhere function do_work(jobs, results)
                        while true
                              index = take!(jobs)
                              step = 100_000_000
                              put!(results, (index, solution((index - 1) * step, index * step)))
                            end
                end

    n = 100
    @async for i in 1:n
            put!(jobs, i)
        end

    for p in workers()
        remote_do(do_work, p, jobs, results)
    end

    total = 0
    while n > 0
        job_id, count = take!(results)
        total += count
        n = n - 1
    end
    println(total)
end


@elapsed problem668Parallel()

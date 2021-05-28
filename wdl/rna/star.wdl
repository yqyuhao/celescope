version 1.0

task star {
    input {
        String sample_name
        File cutadapt_out_fq
        String genomeDir
        File in_data
        Int runtime_cpu_star
        Int runtime_mem_star
    }

    runtime {
        cpu: runtime_cpu_star
        memory: runtime_mem_star + "GiB"
    }

    command {
        set -euo pipefail
        mv "~{in_data}" ".data.json"
        celescope rna star \
        --outdir "03.STAR" \
        --sample "~{sample_name}" \
        --assay rna --fq "~{cutadapt_out_fq}" \
        --genomeDir "~{genomeDir}" \
        --thread ~{runtime_cpu_star} \
        --starMem ~{runtime_mem_star} \
        --outFilterMatchNmin 0
    }

    output {
        File data_json = ".data.json"
        File out_bam = "03.STAR/~{sample_name}_Aligned.sortedByCoord.out.bam"
    }
}